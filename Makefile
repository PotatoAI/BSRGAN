POETRY = poetry run python

download-all-models:
	$(POETRY) main_download_pretrained_models.py --models "all"  --model_dir "model_zoo"

download-BSRGAN-models:
	$(POETRY) main_download_pretrained_models.py --models "BSRGAN"  --model_dir "model_zoo"

mobel_zoo/BSRGAN.pth:
	$(MAKE) download-BSRGAN-models

process-video:
	$(POETRY) video.py input.mp4 output.mp4

upscale:
	$(POETRY) main.py input.png output.png

poetry-install:
	poetry install

setup: poetry-install mobel_zoo/BSRGAN.pth
