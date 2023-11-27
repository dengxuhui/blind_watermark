import os

import blind_watermark

os.chdir(os.path.dirname(__file__))

bwm_encode = blind_watermark.WaterMark()
# 添加水印
bwm_encode.read_img('dengxuhui/game_test.jpeg')
wm = "{user_id:'ETFDAF40',version:'1.11.0(1945)',gen_time:'1701074304',stack_trace:''}"
bwm_encode.read_wm(wm, mode='str')
bwm_encode.embed('output/game_test_embedded.png', 1)

# 解水印
len_wm = len(bwm_encode.wm_bit)
print('Put down the length of wm_bit {len_wm}'.format(len_wm=len_wm))

bwm_decode = blind_watermark.WaterMark()
wm_extract = bwm_decode.extract('output/game_test_embedded.png', wm_shape=len_wm, mode='str')

print("不攻击的提取结果：", wm_extract)

assert wm == wm_extract, '提取水印和原水印不一致'
