import requests
import json

class AnyLanguage:
    """
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
    def INPUT_TYPES(s):
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
                "model": (["gpt-4o-mini", "gpt-4o", "gpt-4-turbo", "gpt-4", "gpt-3.5-turbo"], {
                    "default": "gpt-4o-mini"
                }),
                "translate": (["disable", "enable"], {
                    "default": "enable",
                    "tooltip": "Enable or disable the translation feature."
                }),
                "text": ("STRING", {
                    "multiline": True,
                    "dynamicPrompts": True,
                    "tooltip": "The text to be translated and encoded."
                }),
                "clip": ("CLIP", {"tooltip": "The CLIP model used for encoding the translated text."})
            },
        }

    RETURN_TYPES = ("CONDITIONING",)
    OUTPUT_TOOLTIPS = ("A conditioning containing the embedded translated text used to guide the diffusion model.",)
    FUNCTION = "encode"
    CATEGORY = "conditioning"
    DESCRIPTION = "Translates a text prompt using the OpenAI API and encodes it with a CLIP model into an embedding that can be used to guide the diffusion model towards generating specific images."

    def encode(self, api_key, api_url, model, translate, clip, text):
        """
        Translates the given prompt to English, then encodes it using the CLIP model.

        Parameters:
        api_key (str): The OpenAI API key provided by the user.
        api_url (str): The API URL provided by the user.
        model (str): The model selected by the user from the dropdown menu.
        translate (str): The selection to enable or disable translation.
        clip: The CLIP model used to encode the text.
        text (str): The input prompt to be translated and encoded.

        Returns:
        tuple: A tuple containing the conditioning embedding for the translated text.
        """
        try:
            if translate == "enable":
                headers = {
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {api_key}"
                }
                payload = {
                    "model": model,
                    "messages": [
                        {"role": "system", "content": "You are a translation expert. Your task is to accurately and fluently translate the following text into English, ensuring the translation is optimized for use as a prompt in AI-generated image creation. The translation should be natural, precise, and tailored for generating visual content. Do not add any additional comments or notes."},
                        {"role": "user", "content": text}
                    ]
                }

                response = requests.post(api_url, headers=headers, data=json.dumps(payload))
                response.raise_for_status()  # This will raise an error for bad status codes
                response_data = response.json()

                translated_text = response_data['choices'][0]['message']['content']
                
                if not translated_text:
                    raise ValueError("Translation returned an empty result.")
            else:
                # If translation is disabled, use the original text
                translated_text = text
                
            print(f"Prompt: {translated_text}")
            tokens = clip.tokenize(translated_text)
            output = clip.encode_from_tokens(tokens, return_pooled=True, return_dict=True)
            cond = output.pop("cond")
            return ([[cond, output]], )
        
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return (f"Translation or Encoding error: {str(e)}",)
        except Exception as e:
            print(f"Error: {str(e)}")
            return (f"Translation or Encoding error: {str(e)}",)

# Add custom API routes, using router
from aiohttp import web
from server import PromptServer

@PromptServer.instance.routes.get("/translate")
async def get_translation(request):
    return web.json_response("Translation service is active.")

# A dictionary that contains all nodes you want to export with their names
NODE_CLASS_MAPPINGS = {
    "AnyLanguage": AnyLanguage
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "AnyLanguage": "multilanguage prompt"
}