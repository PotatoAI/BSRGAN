import logging
import os
import torch
import sys

from utils import utils_logger
from utils import utils_image as util

from models.network_rrdbnet import RRDBNet as net

model_name = 'BSRGAN'
scale_factor = 4
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

if __name__ == '__main__':
    input_img_path = sys.argv[1]
    output_img_path = sys.argv[2]

    utils_logger.logger_info('blind_sr_log', log_path='blind_sr_log.log')
    logger = logging.getLogger('blind_sr_log')

    model_path = os.path.join('model_zoo', model_name+'.pth')
    logger.info('{:>16s} : {:s}'.format('Model Name', model_name))

    logger.info('{:>16s} : {:<d}'.format('GPU ID', torch.cuda.current_device()))
    torch.cuda.empty_cache()

    # --------------------------------
    # define network and load model
    # --------------------------------
    model = net(in_nc=3, out_nc=3, nf=64, nb=23, gc=32, sf=scale_factor)  
    model.load_state_dict(torch.load(model_path), strict=True)
    model.eval()

    for k, v in model.named_parameters():
        v.requires_grad = False

    model = model.to(device)
    torch.cuda.empty_cache()

    input_img = util.imread_uint(input_img_path, n_channels=3)
    input_img = util.uint2tensor4(input_img)
    input_img = input_img.to(device)

    output_img = model(input_img)
    output_img = util.tensor2uint(output_img)
    util.imsave(output_img, output_img_path)

    logger.info("Done")
