download-all-models:
	poetry run python main_download_pretrained_models.py --models "all"  --model_dir "model_zoo"

download-BSRGAN-models:
	poetry run python main_download_pretrained_models.py --models "BSRGAN"  --model_dir "model_zoo"
