# ComfyUI Multilanguage Prompt Plugin
# anylanguage


# Demo

![Demo Video](https://raw.githubusercontent.com/ArataAI/anylanguage/master/demo.gif)

This plugin for ComfyUI allows you to translate multi-language prompts into English using the OpenAI API and then encode them with a CLIP model. It integrates seamlessly into ComfyUI, enabling users to generate AI-based image content with translated prompts. The plugin offers customization options such as selecting the API URL, setting the OpenAI API key, choosing the translation model, and toggling the translation feature on or off.

这个ComfyUI插件可以使用OpenAI API将多语言提示词翻译成英文，并使用CLIP模型对其进行编码。插件无缝集成到ComfyUI中，允许用户使用翻译后的提示词生成基于AI的图像内容。插件提供了多种自定义选项，例如选择API URL、设置OpenAI API密钥、选择翻译模型，以及打开或关闭翻译功能。

このComfyUIプラグインは、OpenAI APIを使用して多言語のプロンプトを英語に翻訳し、CLIPモデルでエンコードする機能を提供します。このプラグインはComfyUIにシームレスに統合され、ユーザーが翻訳されたプロンプトを使用してAIベースの画像コンテンツを生成できるようにします。API URLの選択、OpenAI APIキーの設定、翻訳モデルの選択、翻訳機能のオン/オフの切り替えなどのカスタマイズオプションも提供しています。

이 ComfyUI 플러그인은 OpenAI API를 사용하여 여러 언어의 프롬프트를 영어로 번역하고 CLIP 모델로 인코딩하는 기능을 제공합니다. 이 플러그인은 ComfyUI에 원활하게 통합되어, 사용자가 번역된 프롬프트를 사용하여 AI 기반 이미지 콘텐츠를 생성할 수 있도록 합니다. API URL 선택, OpenAI API 키 설정, 번역 모델 선택 및 번역 기능 활성화 또는 비활성화 등의 사용자 정의 옵션을 제공합니다.

## Description

This plugin for ComfyUI allows you to translate multi-language prompts into English using the OpenAI API and then encode them with a CLIP model. It provides customization options such as selecting the API URL, setting the OpenAI API key, choosing the translation model, and toggling the translation feature on or off.

## Installation and Usage

1. **Installation**:
   - Place the `anylanguage.py` file into the `ComfyUI/custom_nodes` directory.
   - Restart ComfyUI to load the plugin.

2. **Loading the Plugin**:
   - In the ComfyUI interface, right-click and select `Add Node -> conditioning -> multilanguage prompt`.
   - The plugin will now be available in your node tree and can replace any previous plugin in your workflow.

3. **Configuration**:
   - **API URL**: Defines the API URL, with the default set to OpenAI's API at `https://api.openai.com/v1/chat/completions`.
   - **API Key**: Set the key obtained from OpenAI. This key is required to use the translation feature. If you don't have a key, you can apply for one at [OpenAI API Keys](https://platform.openai.com/api-keys).
   - **Model**: The default model is `gpt-4o-mini`, which is suitable for most use cases.
   - **Translate**: Toggle the AI translation feature on or off. If disabled, you must enter the prompt in English in the text box below.

## Usage Instructions in Multiple Languages

### English:
To use this plugin, ensure that the `anylanguage.py` file is placed in the `ComfyUI/custom_nodes` directory, and ComfyUI is restarted. After restarting, right-click in the UI, select `Add Node -> conditioning -> multilanguage prompt`, and configure the plugin according to your needs.

### 中文:
使用此插件时，请确保将`anylanguage.py`文件放置在`ComfyUI/custom_nodes`目录中，并重新启动ComfyUI。重启后，在UI中右键单击，选择`Add Node -> conditioning -> multilanguage prompt`，并根据需要配置插件。

### 日本語:
このプラグインを使用するには、`anylanguage.py`ファイルを`ComfyUI/custom_nodes`ディレクトリに配置し、ComfyUIを再起動してください。再起動後、UIで右クリックして、`Add Node -> conditioning -> multilanguage prompt`を選択し、ニーズに合わせてプラグインを設定します。

### 한국어:
이 플러그인을 사용하려면 `anylanguage.py` 파일을 `ComfyUI/custom_nodes` 디렉토리에 배치하고 ComfyUI를 다시 시작하십시오. 다시 시작한 후 UI에서 마우스 오른쪽 버튼을 클릭하고 `Add Node -> conditioning -> multilanguage prompt`를 선택한 다음 필요에 따라 플러그인을 구성하십시오。
