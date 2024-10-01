import requests
import json

class AnyLanguage:
    """
    V1.1.8

    By Peng.Bo
    SAHO Inc.

    A node for translating multi-language prompts into English using OpenAI's API and encoding them with a CLIP model.

    Class methods
    -------------
    INPUT_TYPES (dict):
        Specify input parameters for the node.

    Attributes
    ----------
    RETURN_TYPES (`tuple`):
        The type of each element in the output tuple.
    FUNCTION (`str`):
        The name of the entry-point method. In this case, it will run AnyLanguage().encode().
    CATEGORY (`str`):
        The category the node should appear in the UI.
    DESCRIPTION (`str`):
        A description of the node's functionality.
    """
    
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "api_url": ("STRING", {
                    "multiline": False,
                    "default": "https://api.openai.com/v1/chat/completions",
                    "tooltip": "Enter the API URL here",
                    "lazy": False
                }),
                "api_key": ("STRING", {
                    "multiline": False,
                    "default": "",
                    "placeholder": "Enter your OpenAI API Key here",
                    "lazy": False
                }),
                "model": ([ "gpt-4o-mini","gpt-3.5-turbo", "gpt-4o-2024-08-06", "gpt-4o","gpt-4-turbo", "gpt-4","o1-mini", "o1-preview"], 
                          {
                    "default": "gpt-4o-mini"
                }),
                "multilingual_prompt": ("STRING", {
                    "multiline": True,
                    "dynamicPrompts": True,
                    "tooltip": "The multilingual prompt to be translated and encoded (optional)."
                }),
                "english_prompt": ("STRING", {
                    "multiline": True,
                    "dynamicPrompts": True,
                    "tooltip": "The English prompt to append to the translated prompt (optional)."
                }),
                "clip": ("CLIP", {"tooltip": "The CLIP model used for encoding the translated text."})
            },
            "optional": {
                "additional_output": ("STRING", {
                    "multiline": False,
                    "default": "",
                    "tooltip": "Optional additional output for error messages."
                })
            }
        }

    RETURN_TYPES = ("CONDITIONING", "STRING")
    OUTPUT_NAMES = ("conditioning", "error_message")
    OUTPUT_TOOLTIPS = (
        "A conditioning containing the embedded translated text used to guide the diffusion model.",
        "Error message detailing any issues encountered during API call."
    )
    FUNCTION = "encode"
    CATEGORY = "conditioning"
    DESCRIPTION = "Translates a text prompt using the OpenAI API and encodes it with a CLIP model into an embedding that can be used to guide the diffusion model towards generating specific images."

    def encode(self, api_key, api_url, model, multilingual_prompt, english_prompt, clip, additional_output=None):
        """
        Translates the given multilingual prompt to English, then encodes it using the CLIP model.

        Parameters:
        api_key (str): The OpenAI API key provided by the user.
        api_url (str): The API URL provided by the user.
        model (str): The model selected by the user from the dropdown menu.
        multilingual_prompt (str): The multilingual prompt to be translated and encoded (optional).
        english_prompt (str): The English prompt to append to the translated prompt (optional).
        clip: The CLIP model used to encode the text.
        additional_output (str): Optional additional output.

        Returns:
        tuple: A tuple containing the conditioning embedding and an error message (if any).
        """
        # ANSI color codes
        RED = "\033[91m"
        GREEN = "\033[92m"
        RESET = "\033[0m"

        # Define default prompts
        default_prompt_exception = "a cute 3D style red kitten"
        default_prompt_refusal = "a cute 3D style yellow kitten"

        # Define JSON Schema for Structured Outputs
        structured_json_schema = {
            "type": "object",
            "properties": {
                "translated_text": {
                    "type": "string"
                }
            },
            "required": ["translated_text"],
            "additionalProperties": False
        }

        error_message = ""

        try:
            translated_text = ""

            # Check if the model name contains 'o1' (case-insensitive)
            is_o1_model = "o1" in model.lower()
            # Check if the model name contains '4o' (case-insensitive)
            supports_structured_output = model.lower() in ["gpt-4o-mini", "gpt-4o-2024-08-06"]

            # Construct messages based on model capabilities
            if multilingual_prompt.strip():
                headers = {
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {api_key}"
                }
                
                if is_o1_model:
                    # Models with 'o1' do not support 'system' role
                    # Combine system instructions into the user message
                    user_content = (
                        "You are a translation expert. Your task is to accurately and fluently translate the following text into English, "
                        "ensuring the translation is optimized for use as a prompt in AI-generated image creation. "
                        "The translation should be natural, precise, and tailored for generating visual content. "
                        "Do not add any additional comments or notes. "
                        + multilingual_prompt
                    )
                    messages = [
                        {
                            "role": "user",
                            "content": user_content
                        }
                    ]
                else:
                    # Models that support 'system' role
                    messages = [
                        {
                            "role": "system",
                            "content": "You are a translation expert. Your task is to accurately and fluently translate the following text into English, ensuring the translation is optimized for use as a prompt in AI-generated image creation. The translation should be natural, precise, and tailored for generating visual content. Do not add any additional comments or notes."
                        },
                        {
                            "role": "user",
                            "content": multilingual_prompt
                        }
                    ]

                payload = {
                    "model": model,
                    "messages": messages
                }
                print(f"OpenAI API Request model: {model}")

                if supports_structured_output:
                    payload["response_format"] = {
                        "type": "json_schema",
                        "json_schema": {
                            "name": "translation_response",
                            "strict": True,
                            "schema": structured_json_schema
                        }
                    }

                response = requests.post(api_url, headers=headers, data=json.dumps(payload))
                print(f"OpenAI API Response: {response.status_code}")

                # Attempt to parse the response regardless of status code
                try:
                    response_data = response.json()
                except json.JSONDecodeError:
                    error_message = "Failed to parse JSON response from OpenAI API."
                    print(f"{RED}{error_message}{RESET}")
                    translated_text = default_prompt_refusal
                    return ([[None, None]], error_message)

                if response.status_code == 200:
                    if supports_structured_output:
                        # Handle Structured Outputs
                        if "error" in response_data:
                            # API returned an error
                            error_message = response_data["error"].get("message", "Unknown error. Using default refusal prompt.")
                            print(f"{RED}OpenAI API returned an error: {error_message}{RESET}")
                            print(f"{RED}Using default refusal prompt.{RESET}")
                            translated_text = default_prompt_refusal
                        elif "choices" in response_data and len(response_data["choices"]) > 0:
                            choice = response_data["choices"][0]
                            if "message" in choice and "content" in choice["message"]:
                                # Extract translated_text from the structured response
                                try:
                                    translation_response = choice["message"]["content"]
                                    # Parse the structured JSON response
                                    translation_json = json.loads(translation_response)
                                    translated_text = translation_json.get("translated_text", "").strip()
                                    if not translated_text:
                                        error_message = "Translation result is empty. Using default exception prompt."
                                        print(f"{RED}{error_message}{RESET}")
                                        translated_text = default_prompt_exception
                                except json.JSONDecodeError:
                                    error_message = "Failed to decode structured JSON response. Using default refusal prompt."
                                    print(f"{RED}{error_message}{RESET}")
                                    translated_text = default_prompt_refusal
                            else:
                                # If the expected fields are missing, use refusal default prompt
                                error_message = "Unexpected response format. Using default refusal prompt."
                                print(f"{RED}{error_message}{RESET}")
                                translated_text = default_prompt_refusal
                        else:
                            # If the response format is unexpected, use refusal default prompt
                            error_message = "Unexpected response structure. Using default refusal prompt."
                            print(f"{RED}{error_message}{RESET}")
                            translated_text = default_prompt_refusal
                    else:
                        # Handle Traditional Responses
                        if "error" in response_data:
                            # API returned an error
                            error_message = response_data["error"].get("message", "Unknown error. Using default refusal prompt.")
                            print(f"{RED}OpenAI API returned an error: {error_message}{RESET}")
                            print(f"{RED}Using default refusal prompt.{RESET}")
                            translated_text = default_prompt_refusal
                        elif "choices" in response_data and len(response_data["choices"]) > 0:
                            choice = response_data["choices"][0]
                            if "message" in choice and "content" in choice["message"]:
                                translated_text = choice["message"]["content"].strip()
                                if not translated_text:
                                    # If translation result is empty, use exception default prompt
                                    error_message = "Translation result is empty. Using default exception prompt."
                                    print(f"{RED}{error_message}{RESET}")
                                    translated_text = default_prompt_exception
                            else:
                                # If the expected fields are missing, use refusal default prompt
                                error_message = "Unexpected response format. Using default refusal prompt."
                                print(f"{RED}{error_message}{RESET}")
                                translated_text = default_prompt_refusal
                        else:
                            # If the response format is unexpected, use refusal default prompt
                            error_message = "Unexpected response structure. Using default refusal prompt."
                            print(f"{RED}{error_message}{RESET}")
                            translated_text = default_prompt_refusal
                else:
                    # Non-200 status codes
                    if "error" in response_data and "message" in response_data["error"]:
                        error_message = response_data["error"]["message"]
                    else:
                        error_message = f"Unexpected error with status code {response.status_code}."
                    print(f"{RED}OpenAI API returned an error: {error_message}{RESET}")
                    print(f"{RED}Using default exception prompt.{RESET}")
                    translated_text = default_prompt_exception if "exception" in error_message.lower() else default_prompt_refusal

            # If english_prompt has content, append it to the translated prompt
            if english_prompt.strip():
                if translated_text:
                    translated_text += " " + english_prompt
                else:
                    translated_text = english_prompt

            # If neither multilingual_prompt nor english_prompt has content, use default prompt for exception
            if not translated_text:
                translated_text = default_prompt_exception

            # Print the final prompt being used in green
            print(f"{GREEN}Final Prompt: {translated_text}{RESET}")

            try:
                # Encode the prompt using the CLIP model
                tokens = clip.tokenize(translated_text)
                output = clip.encode_from_tokens(tokens, return_pooled=True, return_dict=True)
                cond = output.pop("cond")
                return ([[cond, output]], error_message)
            except Exception as e:
                # Handle encoding errors
                error_message += f" Encoding failed: {e}. Using default exception prompt."
                print(f"{RED}{error_message}{RESET}")
                translated_text = default_prompt_exception
                print(f"{RED}Final Prompt after encoding failure: {translated_text}{RESET}")
                tokens = clip.tokenize(translated_text)
                try:
                    output = clip.encode_from_tokens(tokens, return_pooled=True, return_dict=True)
                    cond = output.pop("cond")
                    return ([[cond, output]], error_message)
                except Exception as encode_error:
                    # Handle encoding errors
                    error_message += f" Encoding failed: {encode_error}. Using default exception prompt."
                    print(f"{RED}{error_message}{RESET}")
                    translated_text = default_prompt_exception
                    print(f"{RED}Final Prompt after encoding failure: {translated_text}{RESET}")
                    return ([[None, None]], error_message)

        except requests.exceptions.RequestException as e:
            # Handle network-related errors
            if e.response is not None:
                try:
                    error_data = e.response.json()
                    error_message = error_data["error"].get("message", str(e))
                except ValueError:
                    error_message = str(e)
            else:
                error_message = str(e)
            print(f"{RED}Request failed: {error_message}. Using default exception prompt.{RESET}")
            # Use exception default prompt in case of request exception
            translated_text = default_prompt_exception
            print(f"{GREEN}Final Prompt: {translated_text}{RESET}")
            try:
                tokens = clip.tokenize(translated_text)
                output = clip.encode_from_tokens(tokens, return_pooled=True, return_dict=True)
                cond = output.pop("cond")
                return ([[cond, output]], error_message)
            except Exception as encode_error:
                # Handle encoding errors
                error_message += f" Encoding failed: {encode_error}. Using default exception prompt."
                print(f"{RED}{error_message}{RESET}")
                translated_text = default_prompt_exception
                print(f"{RED}Final Prompt after encoding failure: {translated_text}{RESET}")
                return ([[None, None]], error_message)
        except Exception as e:
            # Handle any other unexpected errors
            error_message = f"An unexpected error occurred: {e}. Using default exception prompt."
            print(f"{RED}{error_message}{RESET}")
            # Use exception default prompt in case of any other exception
            translated_text = default_prompt_exception
            print(f"{GREEN}Final Prompt: {translated_text}{RESET}")
            try:
                tokens = clip.tokenize(translated_text)
                output = clip.encode_from_tokens(tokens, return_pooled=True, return_dict=True)
                cond = output.pop("cond")
                return ([[cond, output]], error_message)
            except Exception as encode_error:
                # Handle encoding errors
                error_message += f" Encoding failed: {encode_error}. Using default exception prompt."
                print(f"{RED}{error_message}{RESET}")
                translated_text = default_prompt_exception
                print(f"{RED}Final Prompt after encoding failure: {translated_text}{RESET}")
                return ([[None, None]], error_message)

# Add custom API routes using router
from aiohttp import web
from server import PromptServer

@PromptServer.instance.routes.get("/translate")
async def get_translation(request):
    return web.json_response("Translation service is active.")

# Export all custom nodes and their display names
NODE_CLASS_MAPPINGS = {
    "AnyLanguage": AnyLanguage
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "AnyLanguage": "Multilanguage Prompt Translation"
}