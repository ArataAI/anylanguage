# ComfyUI Multilanguage Prompt Plugin V1.1.8

![UI](https://raw.githubusercontent.com/ArataAI/anylanguage/master/UI.png)

# Demo

![Demo Video](https://raw.githubusercontent.com/ArataAI/anylanguage/master/demo.gif)

This ComfyUI plugin translates non-English prompts into English using the OpenAI API and then combines the translated text with an additional English prompt for AI image generation. Users can input prompts in any language, and the final prompt used will be the translated text plus any provided English prompt.

这个ComfyUI插件将非英语提示词使用OpenAI API翻译成英文，并将其与额外的英文提示词结合，用于AI图像生成。用户可以输入任何语言的提示词，最终用于生成的提示词将是翻译后的文本加上附加的英文提示词。

このComfyUIプラグインは、非英語のプロンプトをOpenAI APIで英語に翻訳し、その翻訳されたテキストに追加の英語プロンプトを組み合わせてAI画像生成に使用します。ユーザーは任意の言語でプロンプトを入力でき、最終的に使用されるプロンプトは、翻訳されたテキストと提供された英語プロンプトを組み合わせたものになります。

이 ComfyUI 플러그인은 비영어 프롬프트를 OpenAI API로 영어로 번역한 다음, 번역된 텍스트에 추가적인 영어 프롬프트를 결합하여 AI 이미지 생성을 위한 프롬프트로 사용합니다. 사용자는 어떤 언어로든 프롬프트를 입력할 수 있으며, 최종적으로 사용되는 프롬프트는 번역된 텍스트와 제공된 영어 프롬프트를 결합한 것입니다.

## Description

This plugin for ComfyUI allows you to translate multi-language prompts into English using the OpenAI API and then encode them with a CLIP model. It is designed to replace the default `CLIP Text Encode (Prompt)` plugin, allowing users to input prompts in multiple languages and have them translated and encoded for AI-based image generation.

## Installation and Usage

1. **Installation**:
   - Place the `anylanguage.py` file into the `ComfyUI/custom_nodes` directory.
   - Restart ComfyUI to load the plugin.

2. **Loading the Plugin**:
   - In the ComfyUI interface, right-click and select `Add Node -> conditioning -> multilanguage prompt`.
   - This plugin will replace the default `CLIP Text Encode (Prompt)` plugin, allowing you to input prompts in multiple languages and customize the final prompt used for AI image generation.

3. **Configuration**:
   - **API URL**: Defines the API URL, with the default set to OpenAI's API at `https://api.openai.com/v1/chat/completions`.
   - **API Key**: Set the key obtained from OpenAI. This key is required to use the translation feature. If you don't have a key, you can apply for one at [OpenAI API Keys](https://platform.openai.com/api-keys).
   - **Model**: The default model is `gpt-4o-mini`, which is suitable for most use cases.
   - **Multilingual Prompt**: Enter a prompt in any language. If provided, this will be automatically translated into English using the OpenAI API.
   - **English Prompt**: Enter additional English text to be appended to the translated prompt. This field is optional and allows for precise control over the final prompt content.

## Usage Instructions in Multiple Languages

### English:
To use this plugin, place the `anylanguage.py` file into the `ComfyUI/custom_nodes` directory, and restart ComfyUI. After restarting, right-click in the UI, select `Add Node -> conditioning -> multilanguage prompt`. This plugin will replace the default `CLIP Text Encode (Prompt)` plugin, allowing you to input prompts in multiple languages and customize the final English prompt for AI-based image generation.

### 中文:
使用此插件时，请将`anylanguage.py`文件放置在`ComfyUI/custom_nodes`目录中，并重新启动ComfyUI。重启后，在UI中右键单击，选择`Add Node -> conditioning -> multilanguage prompt`。此插件将替代默认的`CLIP Text Encode (Prompt)`插件，使您可以输入多语言提示词，并通过附加英文文本来自定义最终的提示词，用于AI生成图像。

### 日本語:
このプラグインを使用するには、`anylanguage.py`ファイルを`ComfyUI/custom_nodes`ディレクトリに配置し、ComfyUIを再起動してください。再起動後、UIで右クリックして、`Add Node -> conditioning -> multilanguage prompt`を選択します。このプラグインは、デフォルトの`CLIP Text Encode (Prompt)`プラグインの代わりに使用され、複数の言語でプロンプトを入力し、追加の英語テキストを使用して最終的なプロンプトをカスタマイズして、AIベースの画像生成に使用できます。

### 한국어:
이 플러그인을 사용하려면 `anylanguage.py` 파일을 `ComfyUI/custom_nodes` 디렉토리에 배치하고 ComfyUI를 다시 시작하십시오. 다시 시작한 후 UI에서 마우스 오른쪽 버튼을 클릭하고 `Add Node -> conditioning -> multilanguage prompt`를 선택하십시오. 이 플러그인은 기본 `CLIP Text Encode (Prompt)` 플러그인을 대체하여 여러 언어로 프롬프트를 입력하고 추가 영어 텍스트를 통해 최종 프롬프트를 맞춤화하여 AI 기반 이미지 생성을 위해 사용할 수 있습니다。



# ComfyUI & Flux.1 Model Usage Guide

## English
If you're unsure how to use ComfyUI or the Flux.1 model, please refer to this article first:

[ComfyUI & Flux.1 Model Usage Guide](https://github.com/ArataAI/anylanguage/wiki)

## 日本語
ComfyUIやFlux.1モデルの使い方がわからない場合は、まずこちらの記事をご覧ください。

[ComfyUI & Flux.1 モデル使用ガイド](https://github.com/ArataAI/anylanguage/wiki)

## 中文
如果你还不知道如何使用ComfyUI或Flux.1模型，请先参考这篇文章。

[ComfyUI & Flux.1 模型使用指南](https://github.com/ArataAI/anylanguage/wiki)

## 한국어
ComfyUI나 Flux.1 모델 사용 방법을 잘 모른다면, 먼저 이 기사를 참고하세요.

[ComfyUI & Flux.1 모델 사용 가이드](https://github.com/ArataAI/anylanguage/wiki)
