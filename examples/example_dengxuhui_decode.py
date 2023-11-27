import os

import blind_watermark

os.chdir(os.path.dirname(__file__))

# 解水印

bwm_decode = blind_watermark.WaterMark()
wm = "{user_id:'xxxxxxxx',version:'x.xx.x(xxxx)',gen_time:'1701074304',stack_trace:''}"
bwm_decode.read_wm(wm, mode="str")
wm_extract = bwm_decode.extract('dengxuhui/compress_from_tinypng.png', mode='str', wm_shape=len(bwm_decode.wm_bit))

print("不攻击的提取结果：", wm_extract)
