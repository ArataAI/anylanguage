# ComfyUI Multilanguage Prompt Plugin

# Demo

![Demo Video](https://raw.githubusercontent.com/ArataAI/anylanguage/master/demo.gif)

This plugin for ComfyUI allows you to translate multi-language prompts into English using the OpenAI API and then encode them with a CLIP model. It integrates seamlessly into ComfyUI, enabling users to generate AI-based image content with translated prompts. The plugin offers customization options such as selecting the API URL, setting the OpenAI API key, choosing the translation model, and toggling the translation feature on or off.

这个ComfyUI插件可以使用OpenAI API将多语言提示词翻译成英文，并使用CLIP模型对其进行编码。插件无缝集成到ComfyUI中，允许用户使用翻译后的提示词生成基于AI的图像内容。插件提供了多种自定义选项，例如选择API URL、设置OpenAI API密钥、选择翻译模型，以及打开或关闭翻译功能。

このComfyUIプラグインは、OpenAI APIを使用して多言語のプロンプトを英語に翻訳し、CLIPモデルでエンコードする機能を提供します。このプラグインはComfyUIにシームレスに統合され、ユーザーが翻訳されたプロンプトを使用してAIベースの画像コンテンツを生成できるようにします。API URLの選択、OpenAI APIキーの設定、翻訳モデルの選択、翻訳機能のオン/オフの切り替えなどのカスタマイズオプションも提供しています。

이 ComfyUI 플러그인은 OpenAI API를 사용하여 여러 언어의 프롬프트를 영어로 번역하고 CLIP 모델로 인코딩하는 기능을 제공합니다. 이 플러그인은 ComfyUI에 원활하게 통합되어, 사용자가 번역된 프롬프트를 사용하여 AI 기반 이미지 콘텐츠를 생성할 수 있도록 합니다. API URL 선택, OpenAI API 키 설정, 번역 모델 선택 및 번역 기능 활성화 또는 비활성화 등의 사용자 정의 옵션을 제공합니다.

## Description

This plugin for ComfyUI allows you to translate multi-language prompts into English using the OpenAI API and then encode them with a CLIP model. It is designed to replace the default `CLIP Text Encode (Prompt)` plugin, allowing users to input prompts in multiple languages and have them translated and encoded for AI-based image generation.

## Installation and Usage

1. **Installation**:
   - Place the `anylanguage.py` file into the `ComfyUI/custom_nodes` directory.
   - Restart ComfyUI to load the plugin.

2. **Loading the Plugin**:
   - In the ComfyUI interface, right-click and select `Add Node -> conditioning -> multilanguage prompt`.
   - This plugin will replace the default `CLIP Text Encode (Prompt)` plugin, allowing you to input prompts in multiple languages.

3. **Configuration**:
   - **API URL**: Defines the API URL, with the default set to OpenAI's API at `https://api.openai.com/v1/chat/completions`.
   - **API Key**: Set the key obtained from OpenAI. This key is required to use the translation feature. If you don't have a key, you can apply for one at [OpenAI API Keys](https://platform.openai.com/api-keys).
   - **Model**: The default model is `gpt-4o-mini`, which is suitable for most use cases.
   - **Translate**: Toggle the AI translation feature on or off. If disabled, you must enter the prompt in English in the text box below.

## Usage Instructions in Multiple Languages

### English:
To use this plugin, place the `anylanguage.py` file into the `ComfyUI/custom_nodes` directory, and restart ComfyUI. After restarting, right-click in the UI, select `Add Node -> conditioning -> multilanguage prompt`. This plugin will replace the default `CLIP Text Encode (Prompt)` plugin, allowing you to input prompts in multiple languages and have them translated and encoded for AI-based image generation.

### 中文:
使用此插件时，请将`anylanguage.py`文件放置在`ComfyUI/custom_nodes`目录中，并重新启动ComfyUI。重启后，在UI中右键单击，选择`Add Node -> conditioning -> multilanguage prompt`。此插件将替代默认的`CLIP Text Encode (Prompt)`插件，使您可以输入多语言提示词，并将其翻译和编码用于AI生成图像。

### 日本語:
このプラグインを使用するには、`anylanguage.py`ファイルを`ComfyUI/custom_nodes`ディレクトリに配置し、ComfyUIを再起動してください。再起動後、UIで右クリックして、`Add Node -> conditioning -> multilanguage prompt`を選択します。このプラグインは、デフォルトの`CLIP Text Encode (Prompt)`プラグインの代わりに使用され、複数の言語でプロンプトを入力して、AIベースの画像生成のために翻訳してエンコードできるようにします。

### 한국어:
이 플러그인을 사용하려면 `anylanguage.py` 파일을 `ComfyUI/custom_nodes` 디렉토리에 배치하고 ComfyUI를 다시 시작하십시오. 다시 시작한 후 UI에서 마우스 오른쪽 버튼을 클릭하고 `Add Node -> conditioning -> multilanguage prompt`를 선택하십시오. 이 플러그인은 기본 `CLIP Text Encode (Prompt)` 플러그인을 대체하여 여러 언어로 프롬프트를 입력하고 AI 기반 이미지 생성을 위해 번역 및 인코딩할 수 있도록 합니다.


### 한국어:
이 플러그인을 사용하려면 `anylanguage.py` 파일을 `ComfyUI/custom_nodes` 디렉토리에 배치하고 ComfyUI를 다시 시작하십시오. 다시 시작한 후 UI에서 마우스 오른쪽 버튼을 클릭하고 `Add Node -> conditioning -> multilanguage prompt`를 선택한 다음 필요에 따라 플러그인을 구성하십시오。

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
