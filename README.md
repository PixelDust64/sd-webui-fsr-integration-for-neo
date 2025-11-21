# AMD FidelityFX Super Resolution (FSR) 1.0 - Forge Edition

**This is a patched fork of the original extension, specifically optimized and fixed for [Stable Diffusion WebUI Forge](https://github.com/lllyasviel/stable-diffusion-webui-forge) (including the Neo branch).**

This extension integrates [AMD FidelityFX Super Resolution (FSR) 1.0](https://gpuopen.com/fidelityfx-superresolution/) upscaling feature into the WebUI. It offers FSR 1.0 Contrast Adaptive Sharpening upscaling at 2x, 3x, and 4x scales, as well as a universal mode that adapts to the scale set in Hires Fix.

## 🔧 Why this fork? (Changelog)

The original extension fails to load in newer versions of WebUI Forge (specifically the "Neo" architecture) due to aggressive optimization in script loading and stricter Python path handling.

**Changes in this version:**
*   **Fixed Initialization:** Implemented `script_callbacks.on_before_ui` to register the upscalers. This ensures FSR appears in the menu even after Forge "cleans" the model lists during startup.
*   **Path Compatibility:** Updated `fidelityfx_tools.py` to correctly detect the extension directory in the new Forge folder structure.
*   **Import Logic:** Fixed Python import errors that prevented the class from being recognized.
*   **Cleaned Code:** Removed redundant debug prints and legacy checks.

## 📥 Installation

1. Open your WebUI Forge.
2. Go to **Extensions** -> **Install from URL**.
3. Paste the URL of this repository.
4. Click **Install** and then **Restart UI** (completely restart the console/bat file if necessary).

The extension will automatically download the `FidelityFX_CLI` executable during the first run. No manual setup is required.

## 🖼️ Usage

You can use it inside:
*   **Hires Fix** (Generation tab)
*   **Extras Tab** (Upscaling)
*   **Img2Img** (Upscaler settings)

![](/images/preview.png)
![](/images/upscalers.png)

## 💻 Platform Support

*   **Windows:** Primary support (Native).
*   **Linux:** Requires `wine` installed in your `PATH`.

## ⚠️ Credits & Acknowledgments

*   **Original Creator:** This extension was originally created by [AndreyRGW](https://github.com/AndreyRGW/sd-webui-fsr-integration). All credits for the original implementation go to him.
*   **Inspiration:** The original idea was inspired by [light-and-ray's Topaz Photo AI integration](https://github.com/light-and-ray/sd-webui-topaz-photo-ai-integration).
*   **Target Platform:** Optimized for [Stable Diffusion WebUI Forge](https://github.com/lllyasviel/stable-diffusion-webui-forge).

![](/images/comparation.jpg)
