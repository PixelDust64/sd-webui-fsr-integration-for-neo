from dataclasses import dataclass
from modules import shared, script_callbacks
from modules.upscaler import Upscaler, UpscalerData
from modules.processing import StableDiffusionProcessingTxt2Img

try:
    from scripts.fidelityfx_tools import runFidelityFX
except ImportError:
    from fidelityfx_tools import runFidelityFX

@dataclass
class Fields:
    scale: int
    resize_x: int = None
    resize_y: int = None

data = [
    Fields(2),
    Fields(3),
    Fields(4),
]

class BaseClass(Upscaler):
    def __init__(self, dirname=None, fields: Fields = None):
        self.name = "FidelityFX"
        self.fields = fields
        self.scalers = []
        
        if fields is not None:
            name_in_ui = f'FidelityFX Super Resolution {self.fields.scale}x'
            self.name = name_in_ui 
            self.scalers = [UpscalerData(name_in_ui, None, self, self.fields.scale)]
        
        super().__init__()

    def do_upscale(self, img, selected_model):
        try:
            if hasattr(self.fields, 'resize_x') and self.fields.resize_x and hasattr(self.fields, 'resize_y') and self.fields.resize_y:
                return runFidelityFX(img=img, scale=None, resize_x=self.fields.resize_x, resize_y=self.fields.resize_y)
            else:
                return runFidelityFX(img=img, scale=self.fields.scale)
        except Exception as e:
            print(f"FidelityFX upscale error: {e}")
            return img

class FidelityFXUniversal(Upscaler):
    def __init__(self, dirname=None):
        self.name = "FidelityFX Universal"
        self.scalers = [UpscalerData('FidelityFX Universal', None, self, None)]
        super().__init__()

    def upscale(self, img, scale, data_path=None, selected_model=None):
        p = getattr(self, 'processing', None)
        if isinstance(p, StableDiffusionProcessingTxt2Img):
            if hasattr(p, 'hr_resize_x') and p.hr_resize_x and hasattr(p, 'hr_resize_y') and p.hr_resize_y:
                return runFidelityFX(img, scale=None, resize_x=p.hr_resize_x, resize_y=p.hr_resize_y)
            elif hasattr(p, 'hr_scale') and p.hr_scale:
                return runFidelityFX(img, scale=p.hr_scale)
        if scale:
            return runFidelityFX(img, scale=scale)
        return img

# Instancias para injeção
fsr_instances = [
    BaseClass(None, data[0]), # 2x
    BaseClass(None, data[1]), # 3x
    BaseClass(None, data[2]), # 4x
    FidelityFXUniversal(None)
]

# Hook para registrar os upscalers após o carregamento inicial do Forge
def register_fsr_upscalers():
    datas = shared.sd_upscalers
    existing_names = [x.name for x in datas]

    for obj in fsr_instances:
        if obj.name not in existing_names:
            datas.append(obj)

script_callbacks.on_before_ui(register_fsr_upscalers)
