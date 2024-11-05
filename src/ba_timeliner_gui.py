import os
import dearpygui.dearpygui as dpg
import io
import sys
import webbrowser
import time
import pyperclip
import tkinter as tk
from tkinter import filedialog
# from PIL import Image

from ba_timeliner_kernel import *
    
BATL_VERSION = '0.10.6'

# 替换输出至debug_log 第1部分
output = io.StringIO()
sys.stdout = output
sys.stderr = output
# 替换输出至debug_log 提前终止
sys.stdout = sys.__stdout__
sys.stderr = sys.__stderr__
output.close()


folder_path_1 = './student_files/'
folder_path_2 = './mission_files/'
folder_path_3 = './texture_files/student_icons/'
if not os.path.exists(folder_path_1):
    os.makedirs(folder_path_1)
if not os.path.exists(folder_path_2):
    os.makedirs(folder_path_2)
if not os.path.exists(folder_path_3):
    os.makedirs(folder_path_3)



                #   ######    ##    ##   ########  
                #  ##    ##   ##    ##      ##     
                #  ##         ##    ##      ##     
                #  ##  ####   ##    ##      ##     
                #  ##  ####   ##    ##      ##     
                #  ##    ##   ##    ##      ##     
                #  ##    ##   ##    ##      ##     
                #   ######     ######    ######## 



dpg.create_context()


def set_font(path):
    global cn_font_tiny
    global cn_font_mini
    global cn_font_small
    global cn_font_medium
    global cn_font_large
    global cn_font_huge
    with dpg.font_registry():
        with dpg.font(path, 18, default_font=True) as cn_font:
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Default)
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Chinese_Full)
            dpg.add_font_range(0x3100, 0x3ff0)
            #手动添加希腊字母
            dpg.add_font_range(0x03b1,0x03c9)
            dpg.add_font_range(0x0391,0x03a9)
            # add specific glyphs
            # ≡ to 0x2261
            dpg.add_font_chars([0x3105, 0x3107, 0x3108, 0x2261])
            # remap や to %
            dpg.add_char_remap(0x3084, 0x0025)
            # 添加制表符
            dpg.add_font_range(0x2500, 0x257f)
        with dpg.font(path, 9, default_font=False) as cn_font_tiny:
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Default)
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Chinese_Full)
            dpg.add_font_range(0x3100, 0x3ff0)
            dpg.add_font_chars([0x3105, 0x3107, 0x3108])
            dpg.add_char_remap(0x3084, 0x0025)
        with dpg.font(path, 12, default_font=False) as cn_font_mini:
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Default)
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Chinese_Full)
            dpg.add_font_range(0x3100, 0x3ff0)
            dpg.add_font_chars([0x3105, 0x3107, 0x3108])
            dpg.add_char_remap(0x3084, 0x0025)
        with dpg.font(path, 15, default_font=False) as cn_font_small:
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Default)
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Chinese_Full)
            dpg.add_font_range(0x3100, 0x3ff0)
            dpg.add_font_chars([0x3105, 0x3107, 0x3108])
            dpg.add_char_remap(0x3084, 0x0025)
        with dpg.font(path, 21, default_font=False) as cn_font_medium:
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Default)
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Chinese_Full)
            dpg.add_font_range(0x3100, 0x3ff0)
            dpg.add_font_chars([0x3105, 0x3107, 0x3108])
            dpg.add_char_remap(0x3084, 0x0025)
        with dpg.font(path, 24, default_font=False) as cn_font_large:
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Default)
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Chinese_Full)
            dpg.add_font_range(0x3100, 0x3ff0)
            dpg.add_font_chars([0x3105, 0x3107, 0x3108])
            dpg.add_char_remap(0x3084, 0x0025)
        with dpg.font(path, 32, default_font=False) as cn_font_huge:
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Default)
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Chinese_Full)
            dpg.add_font_range(0x3100, 0x3ff0)
            dpg.add_font_chars([0x3105, 0x3107, 0x3108])
            dpg.add_char_remap(0x3084, 0x0025)
    dpg.bind_font(cn_font)

try:
    set_font('C:/Windows/Fonts/msyh.ttc')
except:
    try:
        set_font('./msyh.ttc')
    except:
        pass


with dpg.value_registry():    #value注册与初始化
    dpg.add_string_value(tag="temp_student_variable_0",default_value='')
    dpg.add_string_value(tag="temp_student_variable_1",default_value='')
    dpg.add_string_value(tag="temp_student_variable_2",default_value='')
    dpg.add_color_value(tag='temp_student_variable_color',default_value=(255,255,255))
    dpg.add_int_value(tag="temp_student_variable_3",default_value=3)
    dpg.add_int_value(tag="temp_student_variable_4",default_value=90)
    dpg.add_int_value(tag="temp_student_variable_5",default_value=5)
    dpg.add_int4_value(tag="temp_student_variable_6",default_value=(10,10,10))
    dpg.add_int4_value(tag="temp_student_variable_7",default_value=(9,9,9))
    dpg.add_int_value(tag="temp_student_variable_8",default_value=0)
    dpg.add_int4_value(tag="temp_student_variable_9",default_value=(0,0,0))
    dpg.add_int4_value(tag="temp_student_variable_10",default_value=(20,0,0,0))
    dpg.add_string_value(tag="temp_student_variable_11",default_value='默认')
    dpg.add_int_value(tag="temp_student_variable_12",default_value=3)
    dpg.add_float_value(tag="temp_student_variable_13",default_value=0.0)
    dpg.add_float_value(tag="temp_student_variable_14",default_value=0.0)
    dpg.add_string_value(tag="temp_student_variable_15",default_value='默认')
    dpg.add_int_value(tag="temp_student_variable_16",default_value=30)
    dpg.add_float_value(tag="temp_student_variable_17",default_value=0.0)
    dpg.add_float_value(tag="temp_student_variable_18",default_value=0.0)
    dpg.add_string_value(tag="temp_student_variable_19",default_value='')
    dpg.add_string_value(tag="temp_mission_variable_0",default_value='')
    dpg.add_int_value(tag="temp_mission_variable_1",default_value=240)
    dpg.add_int_value(tag="temp_mission_variable_2",default_value=2)
    dpg.add_string_value(tag="temp_mission_variable_3",default_value='')
    dpg.add_bool_value(tag="temp_mission_variable_4",default_value=False)
    dpg.add_string_value(tag="temp_mission_variable_5",default_value='')
    dpg.add_string_value(tag="debug_output_variable",default_value='')
    dpg.add_float_value(tag="simulation_time",default_value=0.0)
    dpg.add_bool_value(tag="simulation_play",default_value=False)
    

# 主题与风格设置
with dpg.theme(tag="main_theme"):
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (29, 151, 236, 80))
        dpg.add_theme_color(dpg.mvThemeCol_FrameBgHovered, (29, 151, 236, 80))
with dpg.theme(tag='main_theme_2'):
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (192, 224, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ChildBg, (192, 224, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_PopupBg, (192, 224, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_Text, (48, 64, 96), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_TitleBg, (192, 192, 192), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_TitleBgActive, (255, 255, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_TitleBgCollapsed, (224, 224, 224), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (96, 192, 248), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_FrameBgHovered, (88, 168, 224), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_FrameBgActive, (80, 144, 200, 128), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_Header, (96, 192, 248), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_SliderGrab, (0, 0, 0, 96), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_SliderGrabActive, (0, 0, 0, 160), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_MenuBarBg, (96, 192, 248), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_Tab, (96, 192, 248), category=dpg.mvThemeCat_Core)
        # dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5, category=dpg.mvThemeCat_Core)
        # dpg.add_theme_style(dpg.mvStyleVar_GrabRounding, 5, category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_FrameBorderSize, 0.2, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_Button, (255, 255, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (224, 224, 224), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (192, 192, 192), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_CheckMark, (64, 64, 64), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_TableHeaderBg, (176, 216, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_TableRowBg, (160, 208, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_TableRowBgAlt, (144, 200, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ScrollbarBg, (128, 144, 192), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrab, (176, 192, 224), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrabHovered, (160, 176, 224), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrabActive, (152, 168, 224), category=dpg.mvThemeCat_Core)
    # with dpg.theme_component(dpg.mvAll, enabled_state=False):
    #     dpg.add_theme_color(dpg.mvThemeCol_Button, (128, 128, 128), category=dpg.mvThemeCat_Core)
    with dpg.theme_component(dpg.mvInputText):
        dpg.add_theme_style(dpg.mvStyleVar_FrameBorderSize, 0, category=dpg.mvThemeCat_Core)
    with dpg.theme_component(dpg.mvInputInt):
        dpg.add_theme_style(dpg.mvStyleVar_FrameBorderSize, 0, category=dpg.mvThemeCat_Core)
    with dpg.theme_component(dpg.mvInputIntMulti):
        dpg.add_theme_style(dpg.mvStyleVar_FrameBorderSize, 0, category=dpg.mvThemeCat_Core)
    with dpg.theme_component(dpg.mvInputFloat):
        dpg.add_theme_style(dpg.mvStyleVar_FrameBorderSize, 0, category=dpg.mvThemeCat_Core)
    with dpg.theme_component(dpg.mvRadioButton):
        dpg.add_theme_style(dpg.mvStyleVar_FrameBorderSize, 0, category=dpg.mvThemeCat_Core)
    with dpg.theme_component(dpg.mvCombo):
        dpg.add_theme_color(dpg.mvThemeCol_Header, (96, 192, 248), category=dpg.mvThemeCat_Core)
    with dpg.theme_component(dpg.mvFileDialog):
        dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (96, 192, 248), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_FrameBgActive, (96, 192, 248), category=dpg.mvThemeCat_Core)

    # with dpg.theme_component(dpg.mvThemeCol_ChildBg)

with dpg.theme(tag="no_vertical_spacing_theme"):
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_style(dpg.mvStyleVar_ItemSpacing, 0, category=dpg.mvThemeCat_Core)
with dpg.theme(tag="small_input_frame_theme"):
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 3, 0, category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_FrameBorderSize, 0, category=dpg.mvThemeCat_Core)
    with dpg.theme_component(dpg.mvAll, enabled_state=False):
        dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 3, 0, category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_FrameBorderSize, 0, category=dpg.mvThemeCat_Core)
with dpg.theme(tag="delete_theme"):
    with dpg.theme_component(dpg.mvButton):
        dpg.add_theme_color(dpg.mvThemeCol_Text, (255,255,255))
        dpg.add_theme_color(dpg.mvThemeCol_Button, (64,0,0))
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (160,0,0))
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (128,0,0))
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 10)
        # dpg.add_theme_style(dpg.mvStyleVar_FramePadding, i*3, i*3)
with dpg.theme(tag="reset_theme"):
    with dpg.theme_component(dpg.mvButton):
        dpg.add_theme_color(dpg.mvThemeCol_Text, (255,96,96))
with dpg.theme(tag='simulation_theme'):
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (192, 224, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_PopupBg, (192, 224, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_Text, (48, 64, 96), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_TitleBgActive, (255, 255, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (96, 192, 248), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_FrameBgHovered, (88, 168, 224), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_FrameBgActive, (80, 144, 200), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_SliderGrab, (0, 0, 0, 96), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_SliderGrabActive, (0, 0, 0, 160), category=dpg.mvThemeCat_Core)
        # dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5, category=dpg.mvThemeCat_Core)
        # dpg.add_theme_style(dpg.mvStyleVar_GrabRounding, 5, category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_FrameBorderSize, 1, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_Button, (255, 255, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (224, 224, 224), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (192, 192, 192), category=dpg.mvThemeCat_Core)
    # with dpg.theme_component(dpg.mvThemeCol_ChildBg)
    with dpg.theme_component(dpg.mvButton):
        # dpg.add_theme_color(dpg.mvThemeCol_Button, (56, 200, 248), category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5, category=dpg.mvThemeCat_Core)
with dpg.theme(tag='simulation_active_theme'):
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_Button, (255, 255, 64), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (224, 224, 56), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (192, 192, 48), category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_FrameBorderSize, 1, category=dpg.mvThemeCat_Core)
    with dpg.theme_component(dpg.mvButton):
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5, category=dpg.mvThemeCat_Core)
with dpg.theme(tag="red_button_theme"):
    with dpg.theme_component(dpg.mvButton):
        dpg.add_theme_color(dpg.mvThemeCol_Button, (255, 0, 0, 160))
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (192, 0, 0, 160))
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (128, 0, 0, 160))
        dpg.add_theme_style(dpg.mvStyleVar_FrameBorderSize, 0, category=dpg.mvThemeCat_Core)
with dpg.theme(tag="orange_button_theme"):
    with dpg.theme_component(dpg.mvButton):
        dpg.add_theme_color(dpg.mvThemeCol_Button, (255, 96, 0, 160))
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (192, 72, 0, 160))
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (128, 48, 0, 160))
        dpg.add_theme_style(dpg.mvStyleVar_FrameBorderSize, 0, category=dpg.mvThemeCat_Core)
with dpg.theme(tag="disabled_button_theme_light"):
    with dpg.theme_component(dpg.mvButton):
        dpg.add_theme_color(dpg.mvThemeCol_Button, (160, 160, 160))
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (160, 160, 160))
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (160, 160, 160))
    with dpg.theme_component(dpg.mvButton, enabled_state=False):
        dpg.add_theme_color(dpg.mvThemeCol_Button, (160, 160, 160))
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (160, 160, 160))
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (160, 160, 160))
with dpg.theme(tag="disabled_button_theme_dark"):
    with dpg.theme_component(dpg.mvButton):
        dpg.add_theme_color(dpg.mvThemeCol_Text, (128, 128, 128))
        dpg.add_theme_color(dpg.mvThemeCol_Button, (32, 32, 32, 160))
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (32, 32, 32, 160))
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (32, 32, 32, 160))
    with dpg.theme_component(dpg.mvButton, enabled_state=False):
        dpg.add_theme_color(dpg.mvThemeCol_Text, (128, 128, 128))
        dpg.add_theme_color(dpg.mvThemeCol_Button, (32, 32, 32, 160))
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (32, 32, 32, 160))
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (32, 32, 32, 160))
with dpg.theme(tag="grey_transparent_button_theme"):
    with dpg.theme_component(dpg.mvButton):
        dpg.add_theme_color(dpg.mvThemeCol_Button, (128, 128, 128, 64))
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (128, 128, 128, 128))
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (128, 128, 128, 192))
        dpg.add_theme_color(dpg.mvThemeCol_Border, (128, 128, 128, 256))
        dpg.add_theme_color(dpg.mvThemeCol_BorderShadow, (128, 128, 128, 0))
        dpg.add_theme_style(dpg.mvStyleVar_FrameBorderSize, 1, category=dpg.mvThemeCat_Core)


main_theme_multiplier = 1    # 用于调整学生对应颜色的有色按钮的颜色。若准备用main_theme，则设为0.75；若准备用main_theme_2，则设为1.0
main_window_theme = 'main_theme_2'
dpg.bind_theme(main_window_theme)
def switch_night_mode(is_night_mode=False):
    global main_theme_multiplier
    global main_window_theme
    if dpg.does_item_exist('night_mode_checkbox'):
        is_night_mode = dpg.get_value('night_mode_checkbox')
    if is_night_mode:
        main_theme_multiplier = 0.75
        main_window_theme = 'main_theme'
    else:
        main_theme_multiplier = 1
        main_window_theme = 'main_theme_2'
    if dpg.does_item_exist(dpg.get_value('main_tab_bar')):
        if dpg.get_item_label(dpg.get_value('main_tab_bar'))=='debug':
            return
    dpg.bind_theme(main_window_theme)
    
    if mission_log_undo_list:
        dpg.bind_item_theme('undo_button', "main_theme" if dpg.get_value('night_mode_checkbox') else "main_theme_2")
    else:
        dpg.bind_item_theme('undo_button', "disabled_button_theme_dark" if dpg.get_value('night_mode_checkbox') else "disabled_button_theme_light")
    if mission_log_redo_list:
        dpg.bind_item_theme('redo_button', "main_theme" if dpg.get_value('night_mode_checkbox') else "main_theme_2")
    else:
        dpg.bind_item_theme('redo_button', "disabled_button_theme_dark" if dpg.get_value('night_mode_checkbox') else "disabled_button_theme_light")


dpg.add_texture_registry(tag="texture_container")
dpg.add_dynamic_texture(64, 64, [0.,0.,0.,1.]*(64*64), parent="texture_container", tag='student_editor_student_icon')
def update_dynamic_texture(texture_name, texture_size, new_img_path, crop=True, bg_color=None):
    img_flattened = crop_and_resize_image(new_img_path, size=texture_size, crop=crop, bg_color=bg_color)
    # if fill_color:    # 若有填充色，则设置为填充后的图片数组
    #     img_flattened_filled = []
    #     for i in range(int(len(img_flattened)/4)):
    #         pixel = img_flattened[i*4:i*4+4]
    #         if pixel[3]<0.3:
    #             pixel = [fill_color[0]/255, fill_color[1]/255, fill_color[2]/255, 1.]
    #         img_flattened_filled += pixel
    #     dpg.set_value(texture_name, img_flattened_filled)
    # else:
    #     dpg.set_value(texture_name, img_flattened)
    dpg.set_value(texture_name, img_flattened)
def load_image_to_texture_registry(img_path, texture_name=None, size=(96,96), crop=True, bg_color=None):
    img_flattened = crop_and_resize_image(img_path, size=size, crop=crop, bg_color=bg_color)
    if not texture_name:
        filename_with_extension = os.path.basename(img_path)
        filename_without_extension = os.path.splitext(filename_with_extension)[0]
        texture_name = filename_without_extension+'_img_texture'
    # if fill_color:    # 若有填充色，则设置为填充后的图片数组
    #     img_flattened_filled = []
    #     for i in range(int(len(img_flattened)/4)):
    #         pixel = img_flattened[i*4, i*4+4]
    #         if pixel[3]<0.5:
    #             pixel = [fill_color[0]/255, fill_color[1]/255, fill_color[2]/255, 1.]
    #         img_flattened_filled += pixel
    #     dpg.add_static_texture(size[0], size[1], img_flattened_filled, parent="texture_container", tag=texture_name)
    # else:
    #     dpg.add_static_texture(size[0], size[1], img_flattened, parent="texture_container", tag=texture_name)
    dpg.add_static_texture(size[0], size[1], img_flattened, parent="texture_container", tag=texture_name)
    
dont_move_img_path = './texture_files/others/dont_move.png'
wtf_bro_img_path = './texture_files/others/wtf_bro.png'
load_image_to_texture_registry(dont_move_img_path, texture_name='dont_move_img_texture', size=(240,120), crop=False)
load_image_to_texture_registry(wtf_bro_img_path, texture_name='wtf_bro_img_texture', size=(80,80))
# load_image_to_texture_registry(dont_move_img_path, size=(240,120))
# dont_move_img_flattened = crop_and_resize_image(dont_move_img_path, size=(96,96))
# dpg.add_static_texture(96, 96, dont_move_img_flattened, tag="dont_move_img_texture")

# update_dynamic_texture('student_editor_student_icon', (64,64), './texture_files/student_icons/Yuuka_Gym_Icon.png')


# 正片开始
with dpg.window(tag='ba_timeliner', width=1200, height=800):
    with dpg.tab_bar(tag='main_tab_bar', callback=lambda:dpg.bind_theme('main_theme') if dpg.get_item_label(dpg.get_value('main_tab_bar'))=='debug' else dpg.bind_theme(main_window_theme)):
        with dpg.tab(label="欢迎页"):
            dpg.add_checkbox(label='深色模式', tag='night_mode_checkbox', parent='ba_timeliner', pos=(1000,5), callback=switch_night_mode)
            dpg.add_text("欢迎使用BATL摸轴工具！（开发中）")
            dpg.bind_item_font(dpg.last_item(), cn_font_huge)
            dpg.add_separator()
            dpg.add_spacer(height=5)
            dpg.add_text("本工具的适用对象包括但不限于：总力战、大决战、制约解除决战等战斗")
            dpg.add_text("本工具的功能包括但不限于：战斗的自行摸轴、实操辅助、作业导入/导出")
            dpg.add_spacer(height=20)
            dpg.add_text("快速入门")
            dpg.bind_item_font(dpg.last_item(), cn_font_huge)
            dpg.add_separator()
            dpg.add_spacer(height=5)
            dpg.add_text("自行摸轴")
            dpg.bind_item_font(dpg.last_item(), cn_font_large)
            dpg.add_text("\t\t第一步（可选）：在“学生创建/编辑”页中创建或编辑学生，并保存至本地")
            dpg.add_text("\t\t第二步：在“作战时间轴”页中输入关卡敌人数据，并选择上场学生")
            dpg.add_text("\t\t第三步：摸轴，参考页面上各信息，根据需要进行添加ex、添加ns、设置费用等操作\n        建议先在游戏内模拟并摸清ns轴和事件轴并填入计划，再开始规划ex轴")
            dpg.add_text("\t\t第四步：参照页面上的计划和实操辅助在游戏内开票凹总力，或导出作业至.csv文件")
            dpg.add_spacer(height=5)
            dpg.add_text("作业导入")
            dpg.bind_item_font(dpg.last_item(), cn_font_large)
            dpg.add_text("\t\t第一步：预先在本地准备好作业（作战计划文件，.csv格式）")
            dpg.add_text("\t\t第二步：在“作战时间轴”页中选择作业数据文件并导入")
            dpg.add_text("\t\t第三步：抄作业，参照页面上的计划和实操辅助在游戏内开票凹总力，或根据需要对其进行修改")
            dpg.add_separator()
            dpg.add_spacer(height=20)
            dpg.add_text("希望本工具能帮到你，祝早日出分，爽拿一档  :D")
            dpg.bind_item_font(dpg.last_item(), cn_font_large)
            dpg.add_image('wtf_bro_img_texture')
            with dpg.tooltip(dpg.last_item()):
                dpg.add_text('“不是，哥们...”')
                dpg.add_text('            —— giga-35b is watching you')
            

                #   ######     ########    ##    ##    ######      ########    ##    ##    ########  
                #  ##    ##       ##       ##    ##    ##   ##     ##          ###   ##       ##     
                #  ##             ##       ##    ##    ##    ##    ##          ####  ##       ##     
                #   ######        ##       ##    ##    ##    ##    ######      ## ## ##       ##     
                #        ##       ##       ##    ##    ##    ##    ##          ##  ####       ##     
                #        ##       ##       ##    ##    ##    ##    ##          ##   ###       ##     
                #  ##    ##       ##       ##    ##    ##   ##     ##          ##    ##       ##     
                #   ######        ##        ######     ######      ########    ##    ##       ##    

        """
        file_name, display_name=None, star=7, lvl=90, 
        skl_ex=5, skl_ns=10, skl_ps=10, skl_ss=10, eq_1=9, eq_2=9, eq_3=9, eq_u=0, 
        pu_hp=0, pu_ak=0, pu_hl=0, aff_1=0, aff_2=0, aff_3=0, aff_4=0, 
        ex_type='damage', ex_cost=0, ex_pre=0, ex_dur=0, ns_type='buff', ns_cd=0, ns_pre=0, ns_dur=0
        """
        with dpg.tab(label="学生创建/编辑"):
            def student_file_selector_callback(sender, app_data):
                # print(app_data)
                file_path = app_data["file_path_name"]
                file_name = app_data["file_name"]
                print(file_path)
                if file_name[-4:]=='.csv':
                    file_name = file_name[:-4]
                else:
                    print('REJECTED: wrong file format')
                    return
                temp_student = load_student_file(file_path)
                if not temp_student:
                    warnings.warn("REJECTED: not valid student file", UserWarning)
                    return

                dpg.set_value('temp_student_variable_0', file_name)
                dpg.set_value('temp_student_variable_1', temp_student.display_name)
                dpg.set_value('temp_student_variable_2', temp_student.img_file_path)
                temp_color = (temp_student.color_r,temp_student.color_g,temp_student.color_b)
                dpg.set_value('temp_student_variable_color', temp_color)

                dpg.set_value('temp_student_variable_3', temp_student.star)
                dpg.set_value('temp_student_variable_4', temp_student.lvl)
                dpg.set_value('temp_student_variable_5', temp_student.skl_ex)
                dpg.set_value('temp_student_variable_6', (temp_student.skl_ns, temp_student.skl_ps, temp_student.skl_ss))
                dpg.set_value('temp_student_variable_7', (temp_student.eq_1, temp_student.eq_2, temp_student.eq_3))
                dpg.set_value('temp_student_variable_8', temp_student.eq_u)
                dpg.set_value('temp_student_variable_9', (temp_student.pu_hp, temp_student.pu_ak, temp_student.pu_hl))
                dpg.set_value('temp_student_variable_10', (temp_student.aff_1, temp_student.aff_2, temp_student.aff_3, temp_student.aff_4))
                
                dpg.set_value('temp_student_variable_11', temp_student.ex_type)
                dpg.set_value('temp_student_variable_12', temp_student.ex_cost)
                dpg.set_value('temp_student_variable_13', temp_student.ex_pre)
                dpg.set_value('temp_student_variable_14', temp_student.ex_dur)
                dpg.set_value('temp_student_variable_15', temp_student.ns_type)
                dpg.set_value('temp_student_variable_16', temp_student.ns_cd)
                dpg.set_value('temp_student_variable_17', temp_student.ns_pre)
                dpg.set_value('temp_student_variable_18', temp_student.ns_dur)
                dpg.set_value('temp_student_variable_19', temp_student.note)

                update_dynamic_texture('student_editor_student_icon', (64,64), temp_student.img_file_path, bg_color=temp_color)


            def student_save_button_callback(sender, app_data):
                file_name = dpg.get_value('temp_student_variable_0')
                student_display_name = dpg.get_value('temp_student_variable_1')
                if student_display_name=='':
                    dpg.show_item("student_no_file_name_popup")
                    return
                if file_name=='':
                    file_path = './student_files/'+student_display_name+'.csv'
                else:
                    file_path = './student_files/'+file_name+'.csv'
                if os.path.exists(file_path):
                    dpg.show_item("student_overwrite_warning_popup")
                    return
                save_student_execute()

            def save_student_execute(sender=None, app_data=None):
                dpg.hide_item("student_overwrite_warning_popup")
                file_name = dpg.get_value('temp_student_variable_0')
                display_name = dpg.get_value('temp_student_variable_1')
                if file_name=='':
                    file_name = display_name
                img_file_path = dpg.get_value('temp_student_variable_2')
                color = dpg.get_value('temp_student_variable_color')

                star = dpg.get_value('temp_student_variable_3')
                lvl = dpg.get_value('temp_student_variable_4')
                skl_ex = dpg.get_value('temp_student_variable_5')
                skl_ns, skl_ps, skl_ss, _ = dpg.get_value('temp_student_variable_6')
                eq_1, eq_2, eq_3, _ = dpg.get_value('temp_student_variable_7')
                eq_u = dpg.get_value('temp_student_variable_8')
                pu_hp, pu_ak, pu_hl, _ = dpg.get_value('temp_student_variable_9')
                aff_1, aff_2, aff_3, aff_4 = dpg.get_value('temp_student_variable_10')
                
                ex_type = dpg.get_value('temp_student_variable_11')
                ex_cost = dpg.get_value('temp_student_variable_12')
                ex_pre = round(dpg.get_value('temp_student_variable_13'),2)
                ex_dur = round(dpg.get_value('temp_student_variable_14'),2)
                ns_type = dpg.get_value('temp_student_variable_15')
                ns_cd = dpg.get_value('temp_student_variable_16')
                ns_pre = round(dpg.get_value('temp_student_variable_17'),2)
                ns_dur = round(dpg.get_value('temp_student_variable_18'),2)
                note = dpg.get_value('temp_student_variable_19')

                temp_student = Student(file_name, display_name, img_file_path, int(color[0]), int(color[1]), int(color[2]), star, lvl, 
                                       skl_ex, skl_ns, skl_ps, skl_ss, eq_1, eq_2, eq_3, eq_u, 
                                       pu_hp, pu_ak, pu_hl, aff_1, aff_2, aff_3, aff_4, 
                                       ex_type, ex_cost, ex_pre, ex_dur, ns_type, ns_cd, ns_pre, ns_dur, note)
                print(temp_student)
                save_student_file(temp_student)
                dpg.set_value('student_file_saved_text', '保存成功！')

            def open_student_files_folder(sender, app_data):
                try:
                    current_dir = os.getcwd()
                    os.startfile(os.path.join(current_dir, 'student_files'))
                except:
                    pass
            
            def student_info_reset_callback(sender, app_data):
                init_value_list = ['', '', '', 3, 90, 5, (10,10,10), (9,9,9), 0, (0,0,0), (20,0,0,0), '默认', 3, 0, 0, '默认', 30, 0, 0]
                for i in range(18):
                    dpg.set_value(f'temp_student_variable_{i}', init_value_list[i])
                dpg.set_value('temp_student_variable_color', (255,255,255))
                update_dynamic_texture('student_editor_student_icon', (64,64), [0.,0.,0.,1.]*(64*64))
            
            def student_file_selector_cn_path():
                current_dir = os.getcwd()
                if is_valid_english_path(current_dir):
                    dpg.show_item("student_file_dialog")
                else:
                    # 初始化Tkinter窗口（隐藏主窗口）
                    root = tk.Tk()
                    root.withdraw()  # 隐藏主窗口

                    # 打开文件选择对话框并获取文件路径
                    file_path = filedialog.askopenfilename(initialdir='./student_files', title='选择学生文件')
                    if not file_path:
                        print('Cancel selecting file')
                        return
                    file_name = file_path.rsplit('/',maxsplit=1)[-1]

                    student_file_selector_callback(None, app_data={"file_name":file_name, "file_path_name":file_path})
            
            def select_student_icon():
                current_dir = os.getcwd()
                # 初始化Tkinter窗口（隐藏主窗口）
                root = tk.Tk()
                root.withdraw()  # 隐藏主窗口

                # 打开文件选择对话框并获取文件路径
                file_path = filedialog.askopenfilename(initialdir='./texture_files/student_icons', title='选择作战计划文件')
                if not file_path:
                    print('Cancel selecting file')
                    return
                file_name = file_path.rsplit('/',maxsplit=1)[-1]
                relative_path = os.path.relpath(file_path, current_dir)

                update_dynamic_texture('student_editor_student_icon', (64,64), relative_path, bg_color=dpg.get_value('temp_student_variable_color'))
                dpg.set_value('temp_student_variable_2', relative_path)
                
            with dpg.window(label="保存失败", width=240, height=120, modal=True, show=False, tag="student_no_file_name_popup", pos=(300,200)):
                with dpg.group(horizontal=True):
                    dpg.add_image('wtf_bro_img_texture')
                    with dpg.group():
                        dpg.add_text("学生名不能为空!")
                        dpg.add_button(label="确认", width=50, height=30, callback=lambda: dpg.hide_item("student_no_file_name_popup"))
            with dpg.window(label="即将覆盖文件", width=300, height=100, modal=True, show=False, tag="student_overwrite_warning_popup", pos=(250,200)):
                dpg.add_text("检测到存在同名文件，是否保存覆盖？")
                with dpg.group(horizontal=True):
                    dpg.add_button(label="取消", width=50, height=30, callback=lambda: dpg.hide_item("student_overwrite_warning_popup"))
                    dpg.add_spacer(width=10)
                    dpg.add_button(label="确认", width=50, height=30, callback=save_student_execute)
            dpg.add_text('学生文件')
            dpg.bind_item_font(dpg.last_item(), cn_font_large)
            with dpg.group(horizontal=True):
                dpg.add_spacer(width=30)
                # dpg.add_button(label="读取本地学生数据", width=160, height=40, callback=lambda: dpg.show_item("student_file_dialog"))
                dpg.add_button(label="读取本地学生数据", width=160, height=40, callback=student_file_selector_cn_path)
                dpg.bind_item_font(dpg.last_item(), cn_font_medium)
                dpg.add_spacer(width=30)
                dpg.add_button(label="保存学生数据至本地", width=180, height=40, callback=student_save_button_callback)
                dpg.bind_item_font(dpg.last_item(), cn_font_medium)
                with dpg.tooltip(dpg.last_item()):
                    dpg.add_text("默认保存路径为  ./student_files/")
                dpg.add_spacer(width=30)
                dpg.add_button(label="打开文件夹", width=110, height=40, callback=open_student_files_folder)
                dpg.bind_item_font(dpg.last_item(), cn_font_medium)
                with dpg.tooltip(dpg.last_item()):
                    dpg.add_text("打开默认保存路径  ./student_files/")
            with dpg.file_dialog(label='选择学生文件（仅英文路径）', default_path='./student_files/', width=750, height=500, file_count=1, directory_selector=False, show=False, callback=student_file_selector_callback, tag="student_file_dialog"):
                dpg.add_file_extension(".csv", color=(96, 160, 64, 255))
            # dpg.add_spacer(height=20)
            with dpg.group(horizontal=True):
                dpg.add_spacer(width=240)
                dpg.add_text('', tag='student_file_saved_text')
            dpg.add_text('文件信息')
            dpg.bind_item_font(dpg.last_item(), cn_font_large)
            with dpg.group(horizontal=True):
                dpg.add_spacer(width=30)
                dpg.add_input_text(label='学生名', width=120, source='temp_student_variable_1')
                dpg.add_spacer(width=30)
                dpg.add_input_text(label='保存文件名', width=150, source='temp_student_variable_0')
                with dpg.tooltip(dpg.last_item()):
                    dpg.add_text("无需文件后缀，可空置，此时会将学生名作为文件名")
                dpg.add_spacer(width=30)
                dpg.add_button(label='重置此页面信息', width=120, callback=student_info_reset_callback)
                dpg.bind_item_theme(dpg.last_item(), 'reset_theme')
                with dpg.tooltip(dpg.last_item()):
                    dpg.add_text("！！！警告：将清空本页面中的输入，若有需要，请先保存！！！", color=(255,64,64))
            with dpg.group(horizontal=True):
                dpg.add_text('基础信息')
                dpg.bind_item_font(dpg.last_item(), cn_font_large)
                dpg.add_text('[?]')
                with dpg.tooltip(dpg.last_item()):
                    dpg.add_text("可以使用默认值，不会影响时间轴模拟，仅保存信息")
            with dpg.group(horizontal=True):
                with dpg.group():
                    with dpg.group(horizontal=True):
                        dpg.add_spacer(width=30)
                        dpg.add_button(label='选择头像图片', width=120, callback=select_student_icon)
                        dpg.add_spacer(width=10)
                        dpg.add_input_text(width=500, enabled=False, source='temp_student_variable_2')
                    dpg.add_spacer(height=2)
                    with dpg.group(horizontal=True):
                        dpg.add_spacer(width=30)
                        dpg.add_color_edit((255, 255, 255), label="颜色", width=200, no_alpha=True, no_inputs=False, source='temp_student_variable_color')
                        with dpg.tooltip(dpg.last_item()):
                            dpg.add_text("用于作战时间轴中的显示")
                        dpg.add_spacer(width=30)
                        dpg.add_text('选择预设颜色：')
                        with dpg.theme(tag='通常按钮主题'):
                            with dpg.theme_component(dpg.mvButton):
                                temp_color_1, temp_color_2, temp_color_3 = 72*main_theme_multiplier, 85*main_theme_multiplier, 130*main_theme_multiplier
                                dpg.add_theme_color(dpg.mvThemeCol_Button, (temp_color_1,temp_color_2,temp_color_3))
                                dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (temp_color_1+32,temp_color_2+32,temp_color_3+32))
                                dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (temp_color_1+56,temp_color_2+56,temp_color_3+56))
                                text_color = (255,255,255) if 0.299*temp_color_1+0.587*temp_color_2+0.114*temp_color_3<128*main_theme_multiplier else (0,0,0)
                                dpg.add_theme_color(dpg.mvThemeCol_Text, text_color)
                                dpg.add_theme_style(dpg.mvStyleVar_FrameBorderSize, 0, category=dpg.mvThemeCat_Core)
                        with dpg.theme(tag='爆发按钮主题'):
                            with dpg.theme_component(dpg.mvButton):
                                temp_color_1, temp_color_2, temp_color_3 = 146*main_theme_multiplier, 1*main_theme_multiplier, 9*main_theme_multiplier
                                dpg.add_theme_color(dpg.mvThemeCol_Button, (temp_color_1,temp_color_2,temp_color_3))
                                dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (temp_color_1+32,temp_color_2+32,temp_color_3+32))
                                dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (temp_color_1+56,temp_color_2+56,temp_color_3+56))
                                text_color = (255,255,255) if 0.299*temp_color_1+0.587*temp_color_2+0.114*temp_color_3<128*main_theme_multiplier else (0,0,0)
                                dpg.add_theme_color(dpg.mvThemeCol_Text, text_color)
                                dpg.add_theme_style(dpg.mvStyleVar_FrameBorderSize, 0, category=dpg.mvThemeCat_Core)
                        with dpg.theme(tag='贯通按钮主题'):
                            with dpg.theme_component(dpg.mvButton):
                                temp_color_1, temp_color_2, temp_color_3 = 190*main_theme_multiplier, 136*main_theme_multiplier, 2*main_theme_multiplier
                                dpg.add_theme_color(dpg.mvThemeCol_Button, (temp_color_1,temp_color_2,temp_color_3))
                                dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (temp_color_1+32,temp_color_2+32,temp_color_3+32))
                                dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (temp_color_1+56,temp_color_2+56,temp_color_3+56))
                                text_color = (255,255,255) if 0.299*temp_color_1+0.587*temp_color_2+0.114*temp_color_3<128*main_theme_multiplier else (0,0,0)
                                dpg.add_theme_color(dpg.mvThemeCol_Text, text_color)
                                dpg.add_theme_style(dpg.mvStyleVar_FrameBorderSize, 0, category=dpg.mvThemeCat_Core)
                        with dpg.theme(tag='神秘按钮主题'):
                            with dpg.theme_component(dpg.mvButton):
                                temp_color_1, temp_color_2, temp_color_3 = 34*main_theme_multiplier, 111*main_theme_multiplier, 157*main_theme_multiplier
                                dpg.add_theme_color(dpg.mvThemeCol_Button, (temp_color_1,temp_color_2,temp_color_3))
                                dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (temp_color_1+32,temp_color_2+32,temp_color_3+32))
                                dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (temp_color_1+56,temp_color_2+56,temp_color_3+56))
                                text_color = (255,255,255) if 0.299*temp_color_1+0.587*temp_color_2+0.114*temp_color_3<128*main_theme_multiplier else (0,0,0)
                                dpg.add_theme_color(dpg.mvThemeCol_Text, text_color)
                                dpg.add_theme_style(dpg.mvStyleVar_FrameBorderSize, 0, category=dpg.mvThemeCat_Core)
                        with dpg.theme(tag='振动按钮主题'):
                            with dpg.theme_component(dpg.mvButton):
                                temp_color_1, temp_color_2, temp_color_3 = 154*main_theme_multiplier, 70*main_theme_multiplier, 168*main_theme_multiplier
                                dpg.add_theme_color(dpg.mvThemeCol_Button, (temp_color_1,temp_color_2,temp_color_3))
                                dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (temp_color_1+32,temp_color_2+32,temp_color_3+32))
                                dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (temp_color_1+56,temp_color_2+56,temp_color_3+56))
                                text_color = (255,255,255) if 0.299*temp_color_1+0.587*temp_color_2+0.114*temp_color_3<128*main_theme_multiplier else (0,0,0)
                                dpg.add_theme_color(dpg.mvThemeCol_Text, text_color)
                                dpg.add_theme_style(dpg.mvStyleVar_FrameBorderSize, 0, category=dpg.mvThemeCat_Core)
                        with dpg.theme(tag='备选按钮主题'):
                            with dpg.theme_component(dpg.mvButton):
                                temp_color_1, temp_color_2, temp_color_3 = 44*main_theme_multiplier, 135*main_theme_multiplier, 0*main_theme_multiplier
                                dpg.add_theme_color(dpg.mvThemeCol_Button, (temp_color_1,temp_color_2,temp_color_3))
                                dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (temp_color_1+32,temp_color_2+32,temp_color_3+32))
                                dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (temp_color_1+56,temp_color_2+56,temp_color_3+56))
                                text_color = (255,255,255) if 0.299*temp_color_1+0.587*temp_color_2+0.114*temp_color_3<128*main_theme_multiplier else (0,0,0)
                                dpg.add_theme_color(dpg.mvThemeCol_Text, text_color)
                                dpg.add_theme_style(dpg.mvStyleVar_FrameBorderSize, 0, category=dpg.mvThemeCat_Core)
                        dpg.add_button(label='通常', callback=lambda: dpg.set_value('temp_student_variable_color', (72,85,130)))
                        dpg.bind_item_theme(dpg.last_item(), '通常按钮主题')
                        dpg.add_button(label='爆发', callback=lambda: dpg.set_value('temp_student_variable_color', (146,1,9)))
                        dpg.bind_item_theme(dpg.last_item(), '爆发按钮主题')
                        dpg.add_button(label='贯通', callback=lambda: dpg.set_value('temp_student_variable_color', (190,136,2)))
                        dpg.bind_item_theme(dpg.last_item(), '贯通按钮主题')
                        dpg.add_button(label='神秘', callback=lambda: dpg.set_value('temp_student_variable_color', (34,111,157)))
                        dpg.bind_item_theme(dpg.last_item(), '神秘按钮主题')
                        dpg.add_button(label='振动', callback=lambda: dpg.set_value('temp_student_variable_color', (154,70,168)))
                        dpg.bind_item_theme(dpg.last_item(), '振动按钮主题')
                        dpg.add_button(label='备选', callback=lambda: dpg.set_value('temp_student_variable_color', (44,135,0)))
                        dpg.bind_item_theme(dpg.last_item(), '备选按钮主题')
                dpg.add_image('student_editor_student_icon')
            with dpg.group(horizontal=True):
                dpg.add_spacer(width=30)
                dpg.add_slider_int(label='星数', width=80, default_value=3, min_value=1, max_value=7, source='temp_student_variable_3')
                with dpg.tooltip(dpg.last_item()):
                    dpg.add_text("专1-3为5-7星")
                dpg.add_spacer(width=146)
                dpg.add_input_int(label='等级', width=40, default_value=90, min_value=1, max_value=100, step=0, source='temp_student_variable_4')
            with dpg.group(horizontal=True):
                dpg.add_spacer(width=30)
                dpg.add_slider_int(label='EX等级', width=80, default_value=5, min_value=1, max_value=5, source='temp_student_variable_5')
                dpg.add_spacer(width=129)
                dpg.add_slider_intx(label='其他技能等级', width=160, default_value=(10,10,10), min_value=1, max_value=10, size=3, source='temp_student_variable_6')
            with dpg.group(horizontal=True):
                dpg.add_spacer(width=30)
                dpg.add_slider_intx(label='装备等级', width=160, default_value=(9,9,9), min_value=0, max_value=9, size=3, source='temp_student_variable_7')
                dpg.add_spacer(width=38)
                dpg.add_slider_int(label='爱用品等级', width=40, default_value=0, min_value=0, max_value=2, source='temp_student_variable_8')
            with dpg.group(horizontal=True):
                dpg.add_spacer(width=30)
                dpg.add_input_intx(label='能力解放等级', width=160, default_value=(0,0,0), min_value=0, max_value=25, size=3, source='temp_student_variable_9')
                dpg.add_spacer(width=10)
                dpg.add_input_intx(label='好感等级', width=160, default_value=(20,0,0,0), min_value=1, max_value=50, size=4, source='temp_student_variable_10')
                with dpg.tooltip(dpg.last_item()):
                    dpg.add_text("包括其他同名学生")
            dpg.add_text('技能信息')
            dpg.bind_item_font(dpg.last_item(), cn_font_large)
            with dpg.group(horizontal=True):
                dpg.add_spacer(width=30)
                with dpg.group():
                    dpg.add_combo(['默认','伤害','buff'], label='EX类型', width=80, default_value='默认', source='temp_student_variable_11')
                    dpg.add_combo(['默认','伤害','buff'], label='NS类型', width=80, default_value='默认', source='temp_student_variable_15')
                dpg.add_spacer(width=30)
                with dpg.group():
                    dpg.add_slider_int(label='EX默认费用', width=80, default_value=3, min_value=0, max_value=10, source='temp_student_variable_12')
                    dpg.add_input_int(label='NS技能CD', width=80, default_value=30, min_value=0, max_value=300, step=0, min_clamped=True, max_clamped=True, source='temp_student_variable_16')
                dpg.add_spacer(width=30)
                with dpg.group():
                    dpg.add_input_float(label='EX前摇(秒)', width=80, default_value=0, format='%.2f', min_value=0, max_value=10, step=0, min_clamped=True, max_clamped=True, source='temp_student_variable_13')
                    with dpg.tooltip(dpg.last_item()):
                        dpg.add_text("高级选项，可忽略。用于设置EX释放到EX实际生效的时间差，不会改变EX持续时间，即EX生效时段会顺延。")
                    dpg.add_input_float(label='NS前摇(秒)', width=80, default_value=0, format='%.2f', min_value=0, max_value=10, step=0, min_clamped=True, max_clamped=True, source='temp_student_variable_17')
                    with dpg.tooltip(dpg.last_item()):
                        dpg.add_text("高级选项，可忽略。用于设置NS释放到NS实际生效的时间差，不会改变NS持续时间，即NS生效时段会顺延。")
                dpg.add_spacer(width=30)
                with dpg.group():
                    dpg.add_input_float(label='EX持续时间(秒)', width=80, default_value=0, format='%.2f', min_value=0, max_value=300, step=0, min_clamped=True, max_clamped=True, source='temp_student_variable_14')
                    dpg.add_input_float(label='NS持续时间(秒)', width=80, default_value=0, format='%.2f', min_value=0, max_value=300, step=0, min_clamped=True, max_clamped=True, source='temp_student_variable_18')
            with dpg.group(horizontal=True):
                dpg.add_text('备注信息')
                dpg.bind_item_font(dpg.last_item(), cn_font_large)
                dpg.add_text('[?]')
                with dpg.tooltip(dpg.last_item()):
                    dpg.add_text("可填写技能使用说明等")
            with dpg.group(horizontal=True):
                dpg.add_spacer(width=30)
                dpg.add_input_text(label='备注', height=100, source='temp_student_variable_19', multiline=True)
            # with dpg.group(horizontal=True):
            #     dpg.add_spacer(width=30)
            #     dpg.add_combo(['默认','伤害','buff'], label='NS类型', width=80, default_value='默认', source='temp_student_variable_14')
            #     dpg.add_spacer(width=30)
            #     dpg.add_input_int(label='NS技能CD', width=80, default_value=30, min_value=0, max_value=300, step=0, min_clamped=True, max_clamped=True, source='temp_student_variable_15')
            #     dpg.add_spacer(width=30)
            #     dpg.add_input_float(label='NS前摇(秒)', width=80, default_value=0, format='%.2f', min_value=0, max_value=10, step=0, min_clamped=True, max_clamped=True, source='temp_student_variable_16')
            #     with dpg.tooltip(dpg.last_item()):
            #         dpg.add_text("高级选项，可忽略。用于设置NS释放到NS实际生效的时间差，不会改变NS持续时间，即NS生效时段会顺延。")
            #     dpg.add_spacer(width=30)
            #     dpg.add_input_float(label='NS持续时间(秒)', width=80, default_value=0, format='%.2f', min_value=0, max_value=300, step=0, min_clamped=True, max_clamped=True, source='temp_student_variable_17')



                #  ##    ##    ########     ######      ######     ########     ######     ##    ##  
                #  ###  ###       ##       ##    ##    ##    ##       ##       ##    ##    ###   ##  
                #  ########       ##       ##          ##             ##       ##    ##    ####  ##  
                #  ## ## ##       ##        ######      ######        ##       ##    ##    ## ## ##  
                #  ##    ##       ##             ##          ##       ##       ##    ##    ##  ####  
                #  ##    ##       ##             ##          ##       ##       ##    ##    ##   ###  
                #  ##    ##       ##       ##    ##    ##    ##       ##       ##    ##    ##    ##  
                #  ##    ##    ########     ######      ######     ########     ######     ##    ##
                        
        """
        {
            'file_name': '猫鬼ins',
            'mission_time': 240,
            'cost_init_delay': 2,
            'cost_timeline': {240: 0, 238: 4200},
            'student_list': [
                ['himari_example', '专二轮椅', 6, 90, 5, 7, 10, 10, 9, 9, 4, 0, 0, 0, 0, 20, 0, 0, 0, 3, True, 30, 1, 15.47, 0, 23],
                ['hanoko_swimsuit_example', '满配水花', 7, 90, 5, 10, 10, 10, 9, 9, 9, 0, 0, 25, 0, 50, 20, 0, 0, 2, True, 30, 1.5, 0.67, 0, 20]
            ],
            'enemy': ['kurokage_example', '猫鬼ins'],
            'student_ex': [
                ['专二轮椅', 225, 2, '满配水花', 'buff', ''],
                ['满配水花', 224, 1, '猫鬼ins', 'damage', ''],
                ['满配水花', 220, None, '猫鬼ins', 'damage', ''],
                ['专二轮椅', 211, None, '满配水花', 'buff', ''],
                ['满配水花', 208, None, '猫鬼ins', 'damage', ''],
                ['满配水花', 200, None, '猫鬼ins', 'damage', '']
            ],
            'student_ns': [
                ['专二轮椅', 210, '猫鬼ins', 'buff', ''],
                ['满配水花', 210, '猫鬼ins', 'buff', '']
            ],
            'enemy_event': [
                [180, 180, '转p2'],
                [120, 120, '转p3']
            ]
        }
        """
        with dpg.tab(label="作战时间轴"):
            temp_mission_log = {
                'file_name': '',
                'mission_time': 240,
                'cost_init_delay': 2,
                'cost_timeline': [[240,0], [238,4200]],
                'cost_direct': [],
                'student_list': [],
                'enemy': ['', ''],
                'student_ex': [],
                'student_ns': [],
                'enemy_event': [],
                'is_udb': False,
                'note': ''
            }
            mission = Mission(log=temp_mission_log)
            mission_log_undo_list = []
            mission_log_redo_list = []
            # mission_undo_list.append(temp_mission_log)
            mission_log_undo_buffer = temp_mission_log.copy()    # 除了每次refresh_battle_plan时变更undo_list和redo_list外，其他时间一直和mission.log同步
            def mission_undo():
                global mission
                global mission_log_undo_list
                global mission_log_redo_list
                global mission_log_undo_buffer
                backup_mission_log = mission.log.copy()
                try:
                    if not mission_log_undo_list:
                        print('mission_log_undo_list is empty, cannot undo')
                        return
                    temp_mission_log = mission_log_undo_list.pop()
                    mission = Mission(log=temp_mission_log)
                    dpg.set_value('temp_mission_variable_0', mission.file_name)
                    dpg.set_value('temp_mission_variable_1', mission.mission_time)
                    dpg.set_value('temp_mission_variable_2', mission.cost_init_delay)
                    dpg.set_value('temp_mission_variable_3', mission.enemy.file_name)
                    dpg.set_value('temp_mission_variable_4', mission.is_udb)
                    dpg.set_value('temp_mission_variable_5', mission.note)
                    mission_log_redo_list.append('dummy')
                    refresh_battle_plan(do_type='undo')
                    mission_log_undo_buffer = temp_mission_log
                    mission_log_redo_list.pop()
                    mission_log_redo_list.append(backup_mission_log)
                except:
                    print('unfo failed')
                    mission = Mission(log=backup_mission_log)
                    dpg.set_value('temp_mission_variable_0', mission.file_name)
                    dpg.set_value('temp_mission_variable_1', mission.mission_time)
                    dpg.set_value('temp_mission_variable_2', mission.cost_init_delay)
                    dpg.set_value('temp_mission_variable_3', mission.enemy.file_name)
                    dpg.set_value('temp_mission_variable_4', mission.is_udb)
                    dpg.set_value('temp_mission_variable_5', mission.note)
                    if mission_log_redo_list[-1]=='dummy':
                        mission_log_redo_list.pop()
                    refresh_battle_plan()
            def mission_redo():
                global mission
                global mission_log_undo_list
                global mission_log_redo_list
                global mission_log_undo_buffer
                backup_mission_log = mission.log.copy()
                try:
                    if not mission_log_redo_list:
                        print('mission_log_redo_list is empty, cannot redo')
                        return
                    temp_mission_log = mission_log_redo_list.pop()
                    mission = Mission(log=temp_mission_log)
                    dpg.set_value('temp_mission_variable_0', mission.file_name)
                    dpg.set_value('temp_mission_variable_1', mission.mission_time)
                    dpg.set_value('temp_mission_variable_2', mission.cost_init_delay)
                    dpg.set_value('temp_mission_variable_3', mission.enemy.file_name)
                    dpg.set_value('temp_mission_variable_4', mission.is_udb)
                    dpg.set_value('temp_mission_variable_5', mission.note)
                    mission_log_undo_list.append('dummy')
                    refresh_battle_plan(do_type='redo')
                    mission_log_undo_buffer = temp_mission_log
                    mission_log_undo_list.pop()
                    mission_log_undo_list.append(backup_mission_log)
                except:
                    print('refo failed')
                    mission = Mission(log=backup_mission_log)
                    dpg.set_value('temp_mission_variable_0', mission.file_name)
                    dpg.set_value('temp_mission_variable_1', mission.mission_time)
                    dpg.set_value('temp_mission_variable_2', mission.cost_init_delay)
                    dpg.set_value('temp_mission_variable_3', mission.enemy.file_name)
                    dpg.set_value('temp_mission_variable_4', mission.is_udb)
                    dpg.set_value('temp_mission_variable_5', mission.note)
                    if mission_log_undo_list[-1]=='dummy':
                        mission_log_undo_list.pop()
                    refresh_battle_plan()


            def mission_file_selector_callback(sender, app_data):
                # global mission_log
                global mission

                file_path = app_data["file_path_name"]
                file_name = app_data["file_name"]
                print(file_path)
                if file_name[-4:]=='.csv':
                    file_name = file_name[:-4]
                else:
                    print('REJECTED: wrong file format')
                    return
                mission = load_mission_file(file_path)
                if not mission:
                    warnings.warn("REJECTED: not valid student file", UserWarning)
                    return
                # mission_log = temp_mission.log
                dpg.set_value('temp_mission_variable_0', file_name)
                dpg.set_value('temp_mission_variable_1', mission.mission_time)
                dpg.set_value('temp_mission_variable_2', mission.cost_init_delay)
                dpg.set_value('temp_mission_variable_3', mission.enemy.file_name)
                dpg.set_value('temp_mission_variable_4', mission.is_udb)
                dpg.set_value('temp_mission_variable_5', mission.note)
                refresh_battle_plan()

            def mission_save_button_callback(sender, app_data):
                file_name = dpg.get_value('temp_mission_variable_0')
                if file_name=='':
                    dpg.show_item("mission_no_file_name_popup")
                    return
                file_path = './mission_files/'+file_name+'.csv'
                if os.path.exists(file_path):
                    dpg.show_item("mission_overwrite_warning_popup")
                    return
                save_mission_execute()

            def save_mission_execute(sender=None, app_data=None):
                global mission
                dpg.hide_item("mission_overwrite_warning_popup")
                temp_mission_log = mission.log.copy()
                temp_mission_log['file_name'] = dpg.get_value('temp_mission_variable_0')
                temp_mission_log['mission_time'] = dpg.get_value('temp_mission_variable_1')
                temp_mission_log['cost_init_delay'] = dpg.get_value('temp_mission_variable_2')
                temp_mission_log['enemy'] = [dpg.get_value('temp_mission_variable_3'),dpg.get_value('temp_mission_variable_3')]
                temp_mission_log['is_udb'] = dpg.get_value('temp_mission_variable_4')
                temp_mission_log['note'] = dpg.get_value('temp_mission_variable_5')
                mission = Mission(log=temp_mission_log)
                print(mission.log)
                save_mission_file(mission)
                dpg.set_value('mission_file_saved_text', '保存成功！')

            def open_mission_files_folder(sender, app_data):
                try:
                    current_dir = os.getcwd()
                    os.startfile(os.path.join(current_dir, 'mission_files'))
                except:
                    pass
            
            def set_mission_time_callback():
                global mission
                temp_mission_log = mission.log.copy()
                temp_mission_log['mission_time'] = dpg.get_value('temp_mission_variable_1')
                temp_mission_log['cost_init_delay'] = dpg.get_value('temp_mission_variable_2')
                temp_mission_log['cost_timeline'] = [[temp_mission_log['mission_time'],0], [temp_mission_log['mission_time']-temp_mission_log['cost_init_delay'],4200]]
                mission = Mission(log=temp_mission_log)
                refresh_battle_plan()
            def set_mission_enemy_name_callback():
                global mission
                mission.change_enemy_name(dpg.get_value('temp_mission_variable_3'))
                # temp_mission_log = mission.log.copy()
                # temp_mission_log['enemy'] = [dpg.get_value('temp_mission_variable_3'),dpg.get_value('temp_mission_variable_3')]
                # mission = Mission(log=temp_mission_log)
                refresh_battle_plan()
            
            def is_udb_checkbox_callback():
                global mission
                temp_mission_log = mission.log.copy()
                temp_mission_log['is_udb'] = dpg.get_value('is_udb_checkbox')
                mission = Mission(log=temp_mission_log)
                refresh_battle_plan()

            def mission_info_reset_callback():
                global mission
                temp_mission_log = {
                    'file_name': '',
                    'mission_time': 240,
                    'cost_init_delay': 2,
                    'is_udb': False,
                    'cost_timeline': [[240,0], [238,4200]],
                    'cost_direct': [],
                    'student_list': [],
                    'enemy': ['', ''],
                    'student_ex': [],
                    'student_ns': [],
                    'enemy_event': []
                }
                mission = Mission(log=temp_mission_log)
                dpg.set_value('temp_mission_variable_0', mission.file_name)
                dpg.set_value('temp_mission_variable_1', mission.mission_time)
                dpg.set_value('temp_mission_variable_2', mission.cost_init_delay)
                dpg.set_value('temp_mission_variable_3', mission.enemy.file_name)
                dpg.set_value('temp_mission_variable_4', mission.is_udb)
                dpg.set_value('temp_mission_variable_5', mission.note)
                refresh_battle_plan()
            
            def mission_file_selector_cn_path():
                current_dir = os.getcwd()
                if is_valid_english_path(current_dir):
                    dpg.show_item("mission_file_dialog")
                else:
                    # 初始化Tkinter窗口（隐藏主窗口）
                    root = tk.Tk()
                    root.withdraw()  # 隐藏主窗口

                    # 打开文件选择对话框并获取文件路径
                    file_path = filedialog.askopenfilename(initialdir='./mission_files', title='选择作战计划文件')
                    if not file_path:
                        print('Cancel selecting file')
                        return
                    file_name = file_path.rsplit('/',maxsplit=1)[-1]

                    mission_file_selector_callback(None, app_data={"file_name":file_name, "file_path_name":file_path})
            
            def student_file_selector_cn_path_2():
                current_dir = os.getcwd()
                if is_valid_english_path(current_dir):
                    dpg.show_item("student_file_dialog_2")
                else:
                    # 初始化Tkinter窗口（隐藏主窗口）
                    root = tk.Tk()
                    root.withdraw()  # 隐藏主窗口

                    # 打开文件选择对话框并获取文件路径
                    file_path = filedialog.askopenfilename(initialdir='./student_files', title='选择学生文件')
                    if not file_path:
                        print('Cancel selecting file')
                        return
                    file_name = file_path.rsplit('/',maxsplit=1)[-1]
                    selections = {file_name:file_path}

                    student_file_selector_callback_2(None, app_data={"file_name":file_name, "file_path_name":file_path, "selections":selections})
                

            with dpg.window(label="保存失败", width=240, height=120, modal=True, show=False, tag="mission_no_file_name_popup", pos=(300,200)):
                with dpg.group(horizontal=True):
                    dpg.add_image('wtf_bro_img_texture')
                    with dpg.group():
                        dpg.add_text("保存文件名不能为空!")
                        dpg.add_button(label="确认", width=50, height=30, callback=lambda: dpg.hide_item("mission_no_file_name_popup"))
            with dpg.window(label="已存在同名学生", width=250, height=100, modal=True, show=False, tag="same_name_student_existed_popup", pos=(300,200)):
                dpg.add_text("当前已存在同名学生，请重新选择！")
                dpg.add_button(label="确认", width=50, height=30, callback=lambda: dpg.hide_item("same_name_student_existed_popup"))
            with dpg.window(label="即将覆盖文件", width=300, height=100, modal=True, show=False, tag="mission_overwrite_warning_popup", pos=(250,200)):
                dpg.add_text("检测到存在同名文件，是否保存覆盖？")
                with dpg.group(horizontal=True):
                    dpg.add_button(label="取消", width=50, height=30, callback=lambda: dpg.hide_item("mission_overwrite_warning_popup"))
                    dpg.add_spacer(width=10)
                    dpg.add_button(label="确认", width=50, height=30, callback=save_mission_execute)
            with dpg.window(label="学生数量已达6人上限", width=540, height=130, modal=True, show=False, tag="student_overloading_popup", pos=(300,200)):
                with dpg.group(horizontal=True):
                    dpg.add_image('wtf_bro_img_texture')
                    with dpg.group():
                        dpg.add_text("警告：继续添加学生将使数量超过6名，部分功能受限制，是否继续？")
                        dpg.add_text("（注：若需进行制约解除决战，请勾选右上方“制约解除决战”选项")
                        with dpg.group(horizontal=True):
                            dpg.add_button(label="取消", width=50, height=30, callback=lambda: dpg.hide_item("student_overloading_popup"))
                            dpg.add_spacer(width=10)
                            dpg.add_button(label="确认", width=50, height=30, callback=student_file_selector_cn_path_2)
                            dpg.bind_item_theme(dpg.last_item(), 'reset_theme')
            with dpg.window(label="学生数量已达10人上限", width=360, height=130, modal=True, show=False, tag="student_overloading_popup_2", pos=(300,200)):
                with dpg.group(horizontal=True):
                    dpg.add_image('wtf_bro_img_texture')
                    with dpg.group():
                        dpg.add_text("警告：继续添加学生将使数量超过10名！")
                        dpg.add_text("    部分功能将出现异常，是否继续？")
                        with dpg.group(horizontal=True):
                            dpg.add_spacer(width=10)
                            dpg.add_button(label="取消", width=50, height=30, callback=lambda: dpg.hide_item("student_overloading_popup_2"))
                            dpg.add_spacer(width=10)
                            dpg.add_button(label="确认", width=50, height=30, callback=student_file_selector_cn_path_2)
                            dpg.bind_item_theme(dpg.last_item(), 'reset_theme')
            with dpg.window(label="多选学生过多", width=350, height=130, modal=True, show=False, tag="multi_student_overloading_popup", pos=(300,200)):
                dpg.add_text("添加所选学生将使学生数量超过6人上限！")
                dpg.add_text("若确认需要添加超出上限的人数，请每次仅添加1人")
                dpg.add_button(label="确认", width=50, height=30, callback=lambda: dpg.hide_item("multi_student_overloading_popup"))
            with dpg.window(label="多选学生过多", width=350, height=130, modal=True, show=False, tag="multi_student_overloading_popup_2", pos=(300,200)):
                dpg.add_text("添加所选学生将使学生数量超过10人上限！")
                dpg.add_text("若确认需要添加超出上限的人数，请每次仅添加1人")
                dpg.add_button(label="确认", width=50, height=30, callback=lambda: dpg.hide_item("multi_student_overloading_popup_2"))

            dpg.add_text('作战计划文件')
            dpg.bind_item_font(dpg.last_item(), cn_font_large)
            with dpg.group(horizontal=True):
                dpg.add_spacer(width=30)
                dpg.add_button(label="读取本地作战计划", width=160, height=40, callback=mission_file_selector_cn_path)
                dpg.bind_item_font(dpg.last_item(), cn_font_medium)
                dpg.add_spacer(width=30)
                dpg.add_button(label="保存作战计划至本地", width=180, height=40, callback=mission_save_button_callback)
                dpg.bind_item_font(dpg.last_item(), cn_font_medium)
                with dpg.tooltip(dpg.last_item()):
                    dpg.add_text("默认保存路径为  ./mission_files/")
                dpg.add_spacer(width=30)
                dpg.add_button(label="打开文件夹", width=110, height=40, callback=open_mission_files_folder)
                dpg.bind_item_font(dpg.last_item(), cn_font_medium)
                with dpg.tooltip(dpg.last_item()):
                    dpg.add_text("打开默认保存路径  ./mission_files/")
            with dpg.file_dialog(label='选择作战计划文件（仅英文路径）', default_path='./mission_files/', width=750, height=500, directory_selector=False, show=False, callback=mission_file_selector_callback, tag="mission_file_dialog"):
                dpg.add_file_extension(".csv", color=(96, 160, 64, 255))
            # dpg.add_spacer(height=20)
            with dpg.group(horizontal=True):
                dpg.add_spacer(width=240)
                dpg.add_text('', tag='mission_file_saved_text')

            dpg.add_text('关卡设置')
            dpg.bind_item_font(dpg.last_item(), cn_font_large)
            with dpg.group(horizontal=True):
                dpg.add_spacer(width=30)
                dpg.add_input_text(label='保存文件名', width=150, source='temp_mission_variable_0')
                with dpg.tooltip(dpg.last_item()):
                    dpg.add_text("无需文件后缀")
                dpg.add_spacer(width=20)
                dpg.add_input_int(label='关卡时间(秒)', width=40, default_value=240, min_value=1, max_value=600, step=0, source='temp_mission_variable_1', callback=set_mission_time_callback)
                with dpg.tooltip(dpg.last_item()):
                    dpg.add_text("！！！警告：修改此值会导致作战计划中的费用轴初始化！！！", color=(255,64,64))
                    dpg.add_text("！！！若已编辑费用轴，修改此值请谨慎！！！", color=(255,64,64))
                dpg.add_spacer(width=20)
                dpg.add_input_int(label='初始回费时延(秒)', width=40, default_value=2, min_value=0, max_value=60, step=0, source='temp_mission_variable_2', callback=set_mission_time_callback)
                with dpg.tooltip(dpg.last_item()):
                    dpg.add_text("大部分战斗开始时都有2秒左右不会回费")
                    dpg.add_text("！！！警告：修改此值会导致作战计划中的费用轴初始化！！！", color=(255,64,64))
                    dpg.add_text("！！！若已编辑费用轴，修改此值请谨慎！！！", color=(255,64,64))
                dpg.add_spacer(width=20)
                dpg.add_input_text(label='敌人名', width=100, source='temp_mission_variable_3', callback=set_mission_enemy_name_callback)
                dpg.add_spacer(width=20)
                dpg.add_checkbox(label='制约解除决战', tag='is_udb_checkbox', source='temp_mission_variable_4', callback=is_udb_checkbox_callback)
                with dpg.tooltip(dpg.last_item()):
                    # dpg.add_text("勾选后会增加上场学生栏位，并将费用上限设为20", color=(255,64,64))
                    # dpg.add_text("学生栏位的前6格为前排，后4格为后排，请注意区分（用于实操模拟）", color=(255,64,64))
                    dpg.add_text("勾选后会增加上场学生栏位，并将费用上限设为20")
                    dpg.add_text("学生栏位的前6格为前排，后4格为后排，请注意主动区分（用于实操模拟）")
                    dpg.add_text("窗口最大化以获得最佳体验")
                dpg.add_spacer(width=20)
                dpg.add_button(label='重置此页面信息', width=120, callback=mission_info_reset_callback)
                dpg.bind_item_theme(dpg.last_item(), 'reset_theme')
                with dpg.tooltip(dpg.last_item()):
                    dpg.add_text("！！！警告：将清空本页面中的输入，若有需要，请先保存！！！", color=(255,64,64))
                # with dpg.tooltip(dpg.last_item()):
                #     dpg.add_text("！！！警告：修改此值会导致作战计划中的费用轴初始化！！！", color=(255,64,64))
                #     dpg.add_text("！！！若已编辑费用轴，修改此值请谨慎！！！", color=(255,64,64))
                #     dpg.add_text("虽然这玩意本应和费用轴没啥关系，但它确实会使费用轴重置（")
                #     dpg.add_text("（在改了在改了")
            with dpg.group(horizontal=True):
                dpg.add_spacer(width=30)
                dpg.add_input_text(label='计划备注', height=40, source='temp_mission_variable_5', multiline=True)
            # dpg.add_spacer(height=20)
            def student_file_selector_callback_2(sender, app_data):
                global mission
                is_udb = dpg.get_value('is_udb_checkbox')
                # file_path = app_data["file_path_name"]
                # print(file_path)
                print(app_data)
                selected_count = len(app_data["selections"].keys())
                if selected_count>1 and (selected_count>6-len(mission.log['student_list']) and not is_udb):
                    dpg.show_item('multi_student_overloading_popup')
                    return
                if selected_count>1 and (selected_count>10-len(mission.log['student_list']) and is_udb):
                    dpg.show_item('multi_student_overloading_popup_2')
                    return
                same_name_count = 0
                for key, value in app_data["selections"].items():
                    file_path = value
                    temp_student = load_student_file(file_path)
                    if temp_student.display_name not in mission.instance_dict.keys():
                        mission.add_sst(Student_Skill_Timeline(temp_student))
                    else:
                        same_name_count += 1
                if same_name_count>0:
                    dpg.show_item('same_name_student_existed_popup')
                refresh_battle_plan()
            def add_student_button_callback(sender, app_data):
                is_udb = dpg.get_value('is_udb_checkbox')
                if len(mission.student_skill_timelines)>=6 and not is_udb:
                    dpg.show_item("student_overloading_popup")
                elif len(mission.student_skill_timelines)>=10 and is_udb:
                    dpg.show_item("student_overloading_popup_2")
                else:
                    student_file_selector_cn_path_2()
            def clear_student_button_callback(sender, app_data):
                global mission
                mission.clear_sst()
                refresh_battle_plan()
            def export_student_button_callback():
                current_time = time.localtime()
                formatted_time = time.strftime('%Y%m%d_%H%M', current_time)
                export_path = './student_files/export_'+formatted_time
                if not os.path.exists(export_path):
                    os.makedirs(export_path)
                for sst in mission.student_skill_timelines:
                    temp_student = sst.student
                    save_student_file(temp_student, export_path)
                dpg.set_value('student_file_exported_text', '已导出')

            # with dpg.group(horizontal=True):
            #     dpg.add_spacer(width=30)
            #     dpg.add_button(label='添加学生', width=80, height=30, callback=add_student_button_callback)
            #     with dpg.file_dialog(default_path='./student_files/', width=750, height=500, directory_selector=False, show=False, callback=student_file_selector_callback_2, tag="student_file_dialog_2"):
            #         dpg.add_file_extension(".csv", color=(96, 160, 64, 255))
            #     dpg.add_spacer(height=20)
            #     dpg.add_button(label='清空学生', width=80, height=30, callback=clear_student_button_callback)


                                #  ######       ####      ##    ##    ########    ##        
                                #  ##   ##     ##  ##     ###   ##    ##          ##        
                                #  ##   ##     ##  ##     ####  ##    ##          ##        
                                #  ######     ##    ##    ## ## ##    ######      ##        
                                #  ##         ########    ##  ####    ##          ##        
                                #  ##         ##    ##    ##   ###    ##          ##        
                                #  ##         ##    ##    ##    ##    ##          ##        
                                #  ##         ##    ##    ##    ##    ########    ########  


            def panel_on_close_callback():
                global mission
                is_changed_flag = False
                for i,ex_info in enumerate(mission.global_ex_timeline):
                    student_display_name = ex_info[1]
                    time_point = ex_info[0]
                    cost = ex_info[5]
                    target = ex_info[2]
                    skl_type = ex_info[6]
                    old_note = ex_info[7]
                    new_note = dpg.get_value(f'panel_note_{i}')
                    if old_note!=new_note:
                        is_changed_flag = True
                        mission.remove_student_ex(student_display_name, time_point)
                        mission.add_student_ex(student_display_name, time_point, cost, target, skl_type, new_note)
                dpg.delete_item('battle_operating_panel')
                if is_changed_flag:
                    refresh_battle_plan()

            def battle_operating_panel_callback(sender, app_data):
                # dpg.delete_item('battle_operating_panel')
                is_udb = dpg.get_value('is_udb_checkbox')
                with dpg.window(label="实操参考面板", width=640, height=760, modal=True, show=True, tag="battle_operating_panel", pos=(50,50), on_close=panel_on_close_callback):
                    with dpg.group(horizontal=True, tag='copy_button_group'):
                        text = f'{mission.file_name}\n序号 \t时间 \t当前费用 \t学生EX\n'
                        text1 = f'{mission.file_name}\n时间 \t当前费用 \t学生EX\n'
                        text2 = f'{mission.file_name}\n时间 \t当前费用 \t学生EX\n'
                        def copy_button_callback(sender, app_data, user_data=0):
                            # nonlocal text
                            # nonlocal text1
                            # nonlocal text2
                            if user_data==0:
                                pyperclip.copy(text)
                            elif user_data==1:
                                pyperclip.copy(text1)
                            elif user_data==2:
                                pyperclip.copy(text2)
                            dpg.set_value('copied_text', '已复制')
                            # dpg.set_value('copied_text', '已复制' if dpg.get_value('copied_text')=='' else '')
                        dpg.add_text("本页面用于实际战斗时的快速参考")
                        dpg.add_button(label='复制到剪贴板', user_data=0, callback=copy_button_callback)
                        dpg.add_button(label='复制精简版', user_data=1, callback=copy_button_callback)
                        dpg.add_button(label='复制带备注精简版', user_data=2, callback=copy_button_callback)
                        dpg.add_text('', tag='copied_text')
                    with dpg.group(horizontal=True, horizontal_spacing=0):
                        dpg.add_text("右侧辅助滑块可快速标记时间点，")
                        dpg.add_button(label='某行橙色高亮')
                        dpg.bind_item_theme(dpg.last_item(), 'orange_button_theme')
                        dpg.add_text("代表费用可能不足以使用该技能")
                    with dpg.group(horizontal=True, horizontal_spacing=0):
                        dpg.add_button(label='某行红色高亮')
                        dpg.bind_item_theme(dpg.last_item(), 'red_button_theme')
                        dpg.add_text("代表技能可能不在备选技能中（若为水花、礼奈等改变技能发牌的学生可视情况忽略）")
                    temp_group = dpg.add_group(horizontal=True)
                    with dpg.table(tag="battle_operating_panel_table", parent=temp_group, resizable=True, policy=dpg.mvTable_SizingFixedFit, header_row=True, no_host_extendX=True, borders_innerH=True, borders_outerH=True, borders_outerV=True):
                        dpg.add_table_column(label='序号')
                        dpg.add_table_column(label='时间      ')
                        dpg.add_table_column(label='当前费用')
                        dpg.add_table_column(label='学生EX及费用')
                        # dpg.add_table_column(label='EX费用')
                        dpg.add_table_column(label='目标')
                        dpg.add_table_column(label='备注(可在此添加/更改)')
                        
                        red_highlight_index_list = []
                        orange_highlight_index_list = []
                        last_1 = ''
                        last_2 = ''
                        last_3 = ''
                        last_4 = ''
                        last_5 = ''
                        for i,ex_info in enumerate(mission.global_ex_timeline):
                            current_time, name, target_name, start_time, end_time, skill_cost, skill_type, note = ex_info
                            if int((mission.mission_time-current_time)*30)<=0:
                                current_cost = round(table_cost_list[int((mission.mission_time-current_time)*30)],1)
                            else:
                                current_cost = round(table_cost_list[int((mission.mission_time-current_time)*30)-1],1)
                            with dpg.table_row():
                                dpg.add_text(i+1)
                                dpg.add_text(second_to_minsec(current_time))
                                dpg.add_text(current_cost)
                                # dpg.add_text(name)
                                with dpg.group():
                                    dpg.add_spacer()
                                    with dpg.group(horizontal=True, horizontal_spacing=0):
                                        # dpg.add_text(f'{skill_cost}| ')
                                        img_path='placeholder_path'
                                        for student_info in mission.log['student_list']:
                                            if student_info[1]==ex_info[1]:
                                                img_path = student_info[2]
                                                break
                                        texture_name = img_path+'_18'
                                        if not dpg.does_alias_exist(texture_name):
                                            load_image_to_texture_registry(img_path, texture_name=texture_name, size=(18,18), crop=True, bg_color=student_info[3:6])
                                        dpg.add_image(texture_name)
                                        with dpg.tooltip(dpg.last_item()):
                                            dpg.add_text(f'EX生效时间段：{second_to_minsec(start_time)}-{second_to_minsec(end_time)}')
                                            dpg.add_text(f'技能类型：{skill_type}')
                                        dpg.add_button(label=name, small=True)
                                        dpg.bind_item_theme(dpg.last_item(),name+'_theme')
                                        with dpg.tooltip(dpg.last_item()):
                                            dpg.add_text(f'EX生效时间段：{second_to_minsec(start_time)}-{second_to_minsec(end_time)}')
                                            dpg.add_text(f'技能类型：{skill_type}')
                                        dpg.add_input_int(width=15, step=0, default_value=ex_info[5], enabled=False)
                                        dpg.bind_item_theme(dpg.last_item(), "small_input_frame_theme")
                                dpg.add_text(target_name)
                                dpg.add_input_text(tag=f'panel_note_{i}', width=200, default_value=note)
                            text += f'{i+1} \t{second_to_minsec(current_time)} \t{current_cost} \t{name}'
                            text1 += f'{second_to_minsec(current_time)} \t{current_cost} \t{name}'
                            text2 += f'{second_to_minsec(current_time)} \t{current_cost} \t{name}'
                            if skill_type=='buff':
                                text += f'(对{target_name})'
                            if note:
                                text += f' {note}'
                                text2 += f' {note}'
                            text += '\n'
                            text1 += '\n'
                            text2 += '\n'

                            if current_cost<skill_cost:
                                orange_highlight_index_list.append(i)
                            if is_udb:
                                if name in [last_1, last_2, last_3, last_4, last_5]:
                                    red_highlight_index_list.append(i)
                            else:
                                if name in [last_1, last_2, last_3]:
                                    red_highlight_index_list.append(i)
                            last_5 = last_4
                            last_4 = last_3
                            last_3 = last_2
                            last_2 = last_1
                            last_1 = name
                        
                        text += f'\n本EX文字轴由BATL摸轴工具v{BATL_VERSION}自动生成'
                        text1 += f'\n本EX文字轴由BATL摸轴工具v{BATL_VERSION}自动生成'
                        text2 += f'\n本EX文字轴由BATL摸轴工具v{BATL_VERSION}自动生成'
                        
                        for index in orange_highlight_index_list:
                            dpg.highlight_table_row("battle_operating_panel_table", index, [255, 96, 0, 100])
                        for index in red_highlight_index_list:
                            dpg.highlight_table_row("battle_operating_panel_table", index, [255, 0, 0, 100])


                    last_row_index = 0
                    def assist_slider_callback(sender, app_data):
                        nonlocal last_row_index
                        row_index = 0
                        slider_time = app_data
                        if len(mission.global_ex_timeline)==0:
                            return
                        for ex_info in mission.global_ex_timeline:
                            if ex_info[0]>slider_time:
                                row_index += 1
                            else:
                                break
                        if len(mission.global_ex_timeline)<=row_index:
                            return
                        if not dpg.is_table_row_highlighted("battle_operating_panel_table", row_index):
                            dpg.unhighlight_table_row("battle_operating_panel_table", last_row_index)
                            dpg.highlight_table_row("battle_operating_panel_table", row_index, [255, 165, 0, 100])
                            last_row_index = row_index
                        else:
                            pass
                    dpg.add_slider_float(parent=temp_group, max_value=mission.mission_time, min_value=0, format='%.1f', default_value=mission.mission_time, width=35, height=28*(1+len(mission.global_ex_timeline)), vertical=True, callback=assist_slider_callback)


                                #   ######     ########    ##    ##    ##    ##    ##            ####      ########    ########     ######     ##    ##  
                                #  ##    ##       ##       ###  ###    ##    ##    ##           ##  ##        ##          ##       ##    ##    ###   ##  
                                #  ##             ##       ########    ##    ##    ##           ##  ##        ##          ##       ##    ##    ####  ##  
                                #   ######        ##       ## ## ##    ##    ##    ##          ##    ##       ##          ##       ##    ##    ## ## ##  
                                #        ##       ##       ##    ##    ##    ##    ##          ########       ##          ##       ##    ##    ##  ####  
                                #        ##       ##       ##    ##    ##    ##    ##          ##    ##       ##          ##       ##    ##    ##   ###  
                                #  ##    ##       ##       ##    ##    ##    ##    ##          ##    ##       ##          ##       ##    ##    ##    ##  
                                #   ######     ########    ##    ##     ######     ########    ##    ##       ##       ########     ######     ##    ## 


            def battle_operating_simulation_callback(sender, app_data):
                dpg.delete_item('battle_operating_simulation')
                is_udb = dpg.get_value('is_udb_checkbox')
                with dpg.window(label="实操模拟", width=820, height=700, modal=True, show=True, tag="battle_operating_simulation", pos=(50,50)):
                    dpg.add_text("本页面用于模拟实际战斗，可自行播放或拖动时间进度条来查看某时刻的情况")
                    with dpg.group(horizontal=True, horizontal_spacing=0):
                        dpg.add_text("本页面中支持 ")
                        dpg.add_button(label='空格', small=True, enabled=False)
                        dpg.add_text(" 暂停，左右方向键 ")
                        dpg.add_button(arrow=True, direction=dpg.mvDir_Left, enabled=False)
                        dpg.add_button(arrow=True, direction=dpg.mvDir_Right, enabled=False)
                        dpg.add_text(" (5s)与 ")
                        dpg.add_button(label='鼠标滚轮', small=True, enabled=False)
                        dpg.add_text(" (1s)控制播放进度，上下方向键 ")
                        dpg.add_button(arrow=True, direction=dpg.mvDir_Up, enabled=False)
                        dpg.add_button(arrow=True, direction=dpg.mvDir_Down, enabled=False)
                        dpg.add_text(" 控制播放速度")

                    with dpg.drawlist(width=800, height=500, tag="simulation_drawlist"):
                        ARROW_COLOR_YELLOW = (255, 165, 0)
                        ARROW_COLOR_BLUE = (0, 160, 255)
                        ARROW_COLOR_ORANGE = (255, 96, 0)
                        ARROW_COLOR_PURPLE = (128, 90, 255)
                        dpg.draw_rectangle((0, 0), (800, 500), color=(255, 255, 255), thickness=3, fill=(32, 32, 32))

                        with dpg.draw_layer():    # 中部学生图标+右上时间显示
                            index_dict = {}
                            central_student_pos_0 = (10, 260)
                            central_student_gap = 101
                            central_student_rectangle_width = 92
                            central_student_rectangle_height = 20
                            central_up_student_pos_0 = (10, 180)
                            up_right_time_pos_0 = (680, 30)
                            up_right_time_pos_1 = (760, 50)
                            central_student_img_length = 20
                            for i,student_info in enumerate(mission.log['student_list']):
                                index_dict[student_info[1]] = i
                                img_path = student_info[2]
                                texture_name = img_path+'_21'
                                if not dpg.does_alias_exist(texture_name):
                                    load_image_to_texture_registry(img_path, texture_name=texture_name, size=(21,21), crop=True, bg_color=student_info[3:6])
                                if i<6:    # 常规作战学生框位置
                                    pos_0 = (central_student_pos_0[0]+i*central_student_gap,central_student_pos_0[1])
                                    pos_1 = (central_student_pos_0[0]+central_student_rectangle_width+i*central_student_gap,central_student_pos_0[1]+central_student_rectangle_height)
                                else:    # 制约解除决战后排支援学生框位置
                                    pos_0 = (central_up_student_pos_0[0]+(i-6)*central_student_gap,central_up_student_pos_0[1])
                                    pos_1 = (central_up_student_pos_0[0]+central_student_rectangle_width+(i-6)*central_student_gap,central_up_student_pos_0[1]+central_student_rectangle_height)
                                dpg.draw_rectangle(pos_0, pos_1, color=(255, 255, 255), thickness=1, fill=student_info[3:6])
                                text_color = (255,255,255) if 0.299*student_info[3]+0.587*student_info[4]+0.114*student_info[5]<128 else (0,0,0)
                                dpg.draw_text((pos_0[0]+20,pos_0[1]), student_info[1], color=text_color, size=18)
                                dpg.draw_image(texture_name, (pos_0[0]+1,pos_0[1]+1), (pos_0[0]+central_student_img_length-1,pos_0[1]+central_student_img_length-1))
                                dpg.add_text('距下次', tag=f'central_next_skill_time_text_{student_info[1]}', parent="battle_operating_simulation", color=(255, 255, 255), pos=(pos_0[0]+10, pos_0[1]+60))
                            enemy_pos_0 = (600,140)
                            enemy_gap = 30
                            enemy_rectangle_width = 100
                            enemy_rectangle_height = 22
                            enemy_pos_1 = (enemy_pos_0[0]+enemy_rectangle_width, enemy_pos_0[1]+enemy_rectangle_height)
                            dpg.draw_rectangle(enemy_pos_0, enemy_pos_1, color=(255, 255, 255), thickness=2, fill=(0,0,0))
                            dpg.draw_text((enemy_pos_0[0]+10,enemy_pos_0[1]), mission.enemy.display_name, color=(255, 255, 255), size=18)
                            dpg.draw_rectangle(up_right_time_pos_0, up_right_time_pos_1, color=(0, 0, 32), thickness=0, fill=(0, 0, 32))
                            dpg.add_text(second_to_minsec(mission.mission_time)+'00', tag='up_right_time_text', parent="battle_operating_simulation", color=(255, 255, 255), pos=(up_right_time_pos_0[0]+24, up_right_time_pos_0[1]+84))
                            dpg.bind_item_font(dpg.last_item(),cn_font_medium)
                            if 'sub_enemy_list' in mission.log.keys():
                                for i,sub_enemy_info in enumerate(mission.log['sub_enemy_list']):
                                    dpg.draw_rectangle([enemy_pos_0[0],enemy_pos_0[1]-(i+1)*enemy_gap], [enemy_pos_1[0],enemy_pos_1[1]-(i+1)*enemy_gap], 
                                                       color=(255, 255, 255), thickness=1, fill=(0,0,0))
                                    dpg.draw_text((enemy_pos_0[0]+10,enemy_pos_0[1]-(i+1)*enemy_gap), sub_enemy_info[1], color=(255, 255, 255), size=18)
                        
                        if not is_udb:
                            with dpg.draw_layer():    # 右下费用条（非制约解除决战）
                                # cost_bar_0_pos_0 = (550,470)
                                # cost_bar_0_pos_1 = (768,480)
                                # cost_bar_0_pos_mask = (332,480)
                                # cost_bar_display_circle_pos = (538,467)
                                # cost_bar_display_text_pos = (533,454)
                                cost_bar_0_pos_0 = (525,470)
                                cost_bar_0_pos_1 = (743,480)
                                cost_bar_0_pos_mask = (307,480)
                                cost_bar_display_circle_pos = (513,467)
                                cost_bar_display_text_pos = (508,454)
                                dpg.draw_rectangle(cost_bar_0_pos_0, cost_bar_0_pos_1, color=(64, 64, 160), thickness=0, fill=(64, 64, 160))
                                # for i in range(10):
                                temp_cost = 0
                                with dpg.draw_node() as bar_mask:
                                    dpg.draw_rectangle(cost_bar_0_pos_0, cost_bar_0_pos_1, color=(96, 192, 248), thickness=0, fill=(96, 192, 248))
                                dpg.apply_transform(bar_mask, dpg.create_translation_matrix([22*int(temp_cost)+20*(temp_cost%1)-218+1, 0]))
                                dpg.draw_rectangle(cost_bar_0_pos_0, cost_bar_0_pos_mask, color=(32, 32, 32), fill=(32, 32, 32))
                                for i in range(1,10):
                                    cost_bar_line_pos_0 = (cost_bar_0_pos_0[0]-1+22*i,cost_bar_0_pos_0[1])
                                    cost_bar_line_pos_1 = (cost_bar_0_pos_0[0]-1+22*i,cost_bar_0_pos_1[1])
                                    dpg.draw_line(cost_bar_line_pos_0, cost_bar_line_pos_1, thickness=2, color=(32,32,80))
                                dpg.draw_circle(cost_bar_display_circle_pos, 13, color=(0,0,0), thickness=1, fill=(48, 48, 96))
                                dpg.draw_text(cost_bar_display_text_pos, 0, tag='cost_num_0', color=(255, 255, 255), size=24, show=True)
                                with dpg.draw_node(tag='cost_num_-1', show=False):     # 若费用小于0，则显示该报错提示
                                    temp_pos_0 = [cost_bar_display_circle_pos[0]-150, cost_bar_display_circle_pos[1]-12]
                                    temp_pos_1 = [temp_pos_0[0]+135, temp_pos_0[1]+23]
                                    dpg.draw_rectangle(temp_pos_0, temp_pos_1, color=(192, 32, 32), thickness=4)
                                    dpg.draw_text(temp_pos_0, ' ！！费用超支  ！！', color=(255, 96, 96), size=20)
                                for i in range(1,10):
                                    dpg.draw_text(cost_bar_display_text_pos, i, tag=f'cost_num_{i}', color=(255, 255, 255), size=24, show=False)
                                dpg.draw_text((cost_bar_display_text_pos[0]-5,cost_bar_display_text_pos[1]+2), 10, tag='cost_num_10', color=(255, 255, 255), size=22, show=False)
                                # dpg.show_item('cost_num_10')
                        else:
                            with dpg.draw_layer():    # 右下费用条（制约解除决战）
                                cost_bar_0_pos_0 = (470,470)
                                cost_bar_0_pos_1 = (768,480)
                                cost_bar_0_pos_mask = (172,480)
                                cost_bar_display_circle_pos = (458,467)
                                cost_bar_display_text_pos = (453,454)
                                dpg.draw_rectangle(cost_bar_0_pos_0, cost_bar_0_pos_1, color=(64, 64, 160), thickness=0, fill=(64, 64, 160))
                                # for i in range(10):
                                temp_cost = 0
                                with dpg.draw_node() as bar_mask:
                                    dpg.draw_rectangle(cost_bar_0_pos_0, cost_bar_0_pos_1, color=(96, 192, 248), thickness=0, fill=(96, 192, 248))
                                dpg.apply_transform(bar_mask, dpg.create_translation_matrix([15*int(temp_cost)+13*(temp_cost%1)-298+1, 0]))
                                dpg.draw_rectangle(cost_bar_0_pos_0, cost_bar_0_pos_mask, color=(32, 32, 32), fill=(32, 32, 32))
                                for i in range(1,20):
                                    cost_bar_line_pos_0 = (cost_bar_0_pos_0[0]-1+15*i,cost_bar_0_pos_0[1])
                                    cost_bar_line_pos_1 = (cost_bar_0_pos_0[0]-1+15*i,cost_bar_0_pos_1[1])
                                    dpg.draw_line(cost_bar_line_pos_0, cost_bar_line_pos_1, thickness=2, color=(32,32,80))
                                dpg.draw_circle(cost_bar_display_circle_pos, 13, color=(0,0,0), thickness=1, fill=(48, 48, 96))
                                dpg.draw_text(cost_bar_display_text_pos, 0, tag='cost_num_0', color=(255, 255, 255), size=24, show=True)
                                with dpg.draw_node(tag='cost_num_-1', show=False):     # 若费用小于0，则显示该报错提示
                                    temp_pos_0 = [cost_bar_display_circle_pos[0]-150, cost_bar_display_circle_pos[1]-12]
                                    temp_pos_1 = [temp_pos_0[0]+135, temp_pos_0[1]+23]
                                    dpg.draw_rectangle(temp_pos_0, temp_pos_1, color=(192, 32, 32), thickness=4)
                                    dpg.draw_text(temp_pos_0, ' ！！费用超支  ！！', color=(255, 96, 96), size=20)
                                for i in range(1,10):
                                    dpg.draw_text(cost_bar_display_text_pos, i, tag=f'cost_num_{i}', color=(255, 255, 255), size=24, show=False)
                                for i in range(10,21):
                                    dpg.draw_text((cost_bar_display_text_pos[0]-5,cost_bar_display_text_pos[1]+2), i, tag=f'cost_num_{i}', color=(255, 255, 255), size=22, show=False)
                                # dpg.show_item('cost_num_10')

                        with dpg.draw_layer():    # 右下技能队列
                            # last_skill_frame_pos_0 = (550,425)
                            # last_skill_frame_pos_1 = (630,450)
                            # next_skill_frame_pos_0 = (630,425)
                            # next_skill_frame_pos_1 = (710,450)
                            # then_skill_frame_pos_0 = (680,400)
                            # then_skill_frame_pos_1 = (760,425)
                            skill_frame_width = 105
                            skill_frame_height = 25
                            skill_frame_img_length = 25
                            anchor_1 = (525,425)
                            anchor_2 = (anchor_1[0]+skill_frame_width+25,anchor_1[1]-skill_frame_height)
                            last_skill_frame_pos_0 = (anchor_1[0],anchor_1[1])
                            last_skill_frame_pos_1 = (anchor_1[0]+skill_frame_width,anchor_1[1]+skill_frame_height)
                            next_skill_frame_pos_0 = (anchor_1[0]+skill_frame_width,anchor_1[1])
                            next_skill_frame_pos_1 = (anchor_1[0]+2*skill_frame_width,anchor_1[1]+skill_frame_height)
                            then_skill_frame_pos_0 = (anchor_2[0],anchor_2[1])
                            then_skill_frame_pos_1 = (anchor_2[0]+skill_frame_width,anchor_2[1]+skill_frame_height)
                            dpg.draw_rectangle(last_skill_frame_pos_0, last_skill_frame_pos_1, color=ARROW_COLOR_YELLOW, thickness=2)
                            dpg.draw_rectangle(next_skill_frame_pos_0, next_skill_frame_pos_1, color=ARROW_COLOR_BLUE, thickness=3)
                            for i in range(4):
                                dpg.draw_rectangle((then_skill_frame_pos_0[0],then_skill_frame_pos_0[1]-i*25), (then_skill_frame_pos_1[0],then_skill_frame_pos_1[1]-i*25), color=(255, 255, 255), thickness=2)
                            dpg.add_text('已释放', tag='last_skill_text', parent="battle_operating_simulation", color=(255, 255, 255), pos=(last_skill_frame_pos_0[0]+10, last_skill_frame_pos_0[1]+108))
                            dpg.add_text('将释放', tag='next_skill_text', parent="battle_operating_simulation", color=(255, 255, 255), pos=(next_skill_frame_pos_0[0]+10, next_skill_frame_pos_0[1]+108))
                            for i in range(4):
                                dpg.add_text('', tag=f'then_{i}_skill_text', parent="battle_operating_simulation", color=(255, 255, 255), pos=(then_skill_frame_pos_0[0]+115, then_skill_frame_pos_1[1]-i*25+63))
                            for student_info in mission.log['student_list']:
                                text_color = (255,255,255) if 0.299*student_info[3]+0.587*student_info[4]+0.114*student_info[5]<128 else (0,0,0)
                                img_path = student_info[2]
                                texture_name = img_path+'_21'
                                if not dpg.does_alias_exist(texture_name):
                                    load_image_to_texture_registry(img_path, texture_name=texture_name, size=(21,21), crop=True, bg_color=student_info[3:6])
                                dpg.draw_rectangle(last_skill_frame_pos_0, last_skill_frame_pos_1, tag=f'last_skill_{student_info[1]}_rectangle', color=ARROW_COLOR_YELLOW, thickness=2, fill=student_info[3:6], show=False)
                                dpg.draw_text((last_skill_frame_pos_0[0]+2+skill_frame_img_length,last_skill_frame_pos_0[1]+2), student_info[1], tag=f'last_skill_{student_info[1]}_text', color=text_color, size=18, show=False)
                                dpg.draw_image(texture_name, (last_skill_frame_pos_0[0]+2,last_skill_frame_pos_0[1]+2), (last_skill_frame_pos_0[0]+skill_frame_img_length-2,last_skill_frame_pos_0[1]+skill_frame_img_length-2), tag=f'last_skill_{student_info[1]}_image', show=False)
                                # dpg.add_text(f'{student_info[1]}EX', tag=f'last_skill_{student_info[1]}_text', parent="battle_operating_simulation", color=(255, 255, 255), pos=(last_skill_frame_pos_0[0]+10, last_skill_frame_pos_0[1]+108))
                                dpg.draw_rectangle(next_skill_frame_pos_0, next_skill_frame_pos_1, tag=f'next_skill_{student_info[1]}_rectangle', color=ARROW_COLOR_BLUE, thickness=3, fill=student_info[3:6], show=False)
                                dpg.draw_text((next_skill_frame_pos_0[0]+2+skill_frame_img_length,next_skill_frame_pos_0[1]+2), student_info[1], tag=f'next_skill_{student_info[1]}_text', color=text_color, size=18, show=False)
                                dpg.draw_image(texture_name, (next_skill_frame_pos_0[0]+2,next_skill_frame_pos_0[1]+2), (next_skill_frame_pos_0[0]+skill_frame_img_length-2,next_skill_frame_pos_0[1]+skill_frame_img_length-2), tag=f'next_skill_{student_info[1]}_image', show=False)
                                for i in range(4):
                                    dpg.draw_rectangle((then_skill_frame_pos_0[0],then_skill_frame_pos_0[1]-i*25), (then_skill_frame_pos_1[0],then_skill_frame_pos_1[1]-i*25), tag=f'then_{i}_skill_{student_info[1]}_rectangle', color=(255, 255, 255), thickness=2, fill=student_info[3:6], show=False)
                                    dpg.draw_text((then_skill_frame_pos_0[0]+2+skill_frame_img_length,then_skill_frame_pos_0[1]-i*25+2), student_info[1], tag=f'then_{i}_skill_{student_info[1]}_text', color=text_color, size=18, show=False)
                                    dpg.draw_image(texture_name, (then_skill_frame_pos_0[0]+2,then_skill_frame_pos_0[1]-i*25+2), (then_skill_frame_pos_0[0]+skill_frame_img_length-2,then_skill_frame_pos_0[1]+skill_frame_img_length-i*25-2), tag=f'then_{i}_skill_{student_info[1]}_image', show=False)
                        
                        
                        with dpg.draw_layer():    # 中部技能箭头、学生指示框
                            for i,student_info in enumerate(mission.log['student_list']):
                                if i<6:    # 常规作战位置
                                    dpg.draw_arrow((central_student_pos_0[0]+central_student_rectangle_width+i*central_student_gap-20,central_student_pos_0[1]+central_student_rectangle_height),
                                                (last_skill_frame_pos_0[0]+12,last_skill_frame_pos_0[1]),
                                                tag=f'last_skill_arrow_{student_info[1]}',
                                                show=False,
                                                thickness=1,
                                                size=8,
                                                color=ARROW_COLOR_YELLOW
                                    )
                                    dpg.draw_arrow((central_student_pos_0[0]+central_student_rectangle_width+i*central_student_gap-20,central_student_pos_0[1]+central_student_rectangle_height),
                                                (next_skill_frame_pos_0[0]+12,next_skill_frame_pos_0[1]),
                                                tag=f'next_skill_arrow_{student_info[1]}',
                                                show=False,
                                                thickness=3,
                                                size=10,
                                                color=ARROW_COLOR_BLUE
                                    )
                                    # index_dict[student_info[1]] = i
                                    pos_0 = (central_student_pos_0[0]+i*central_student_gap-5,central_student_pos_0[1]-5)
                                    pos_1 = (central_student_pos_0[0]+central_student_rectangle_width+i*central_student_gap+5,central_student_pos_0[1]+central_student_rectangle_height+5)
                                    # 这里故意交换last和next的顺序，防止细框last被粗框next遮住
                                    dpg.draw_rectangle(pos_0, pos_1, color=ARROW_COLOR_BLUE, thickness=3, tag=f'next_skill_student_frame_{student_info[1]}', show=False)
                                    dpg.draw_rectangle(pos_0, pos_1, color=ARROW_COLOR_YELLOW, thickness=1, tag=f'last_skill_student_frame_{student_info[1]}', show=False)
                                else:    # 制约解除决战后排支援位置
                                    dpg.draw_arrow((central_up_student_pos_0[0]+central_student_rectangle_width+(i-6)*central_student_gap-20,central_up_student_pos_0[1]+central_student_rectangle_height),
                                                (last_skill_frame_pos_0[0]+12,last_skill_frame_pos_0[1]),
                                                tag=f'last_skill_arrow_{student_info[1]}',
                                                show=False,
                                                thickness=1,
                                                size=8,
                                                color=ARROW_COLOR_YELLOW
                                    )
                                    dpg.draw_arrow((central_up_student_pos_0[0]+central_student_rectangle_width+(i-6)*central_student_gap-20,central_up_student_pos_0[1]+central_student_rectangle_height),
                                                (next_skill_frame_pos_0[0]+12,next_skill_frame_pos_0[1]),
                                                tag=f'next_skill_arrow_{student_info[1]}',
                                                show=False,
                                                thickness=3,
                                                size=10,
                                                color=ARROW_COLOR_BLUE
                                    )
                                    # index_dict[student_info[1]] = i
                                    pos_0 = (central_up_student_pos_0[0]+(i-6)*central_student_gap-5,central_up_student_pos_0[1]-5)
                                    pos_1 = (central_up_student_pos_0[0]+central_student_rectangle_width+(i-6)*central_student_gap+5,central_up_student_pos_0[1]+central_student_rectangle_height+5)
                                    # 这里故意交换last和next的顺序，防止细框last被粗框next遮住
                                    dpg.draw_rectangle(pos_0, pos_1, color=ARROW_COLOR_BLUE, thickness=3, tag=f'next_skill_student_frame_{student_info[1]}', show=False)
                                    dpg.draw_rectangle(pos_0, pos_1, color=ARROW_COLOR_YELLOW, thickness=1, tag=f'last_skill_student_frame_{student_info[1]}', show=False)
                            dpg.draw_arrow((enemy_pos_1[0]-50,enemy_pos_1[1]),
                                           (last_skill_frame_pos_0[0]+12,last_skill_frame_pos_0[1]),
                                           tag=f'last_skill_arrow_{mission.enemy.display_name}',
                                           show=False,
                                           thickness=1,
                                           size=8,
                                           color=ARROW_COLOR_ORANGE
                            )
                            dpg.draw_arrow((enemy_pos_1[0]-50,enemy_pos_1[1]),
                                           (next_skill_frame_pos_0[0]+12,next_skill_frame_pos_0[1]),
                                           tag=f'next_skill_arrow_{mission.enemy.display_name}',
                                           show=False,
                                           thickness=3,
                                           size=10,
                                           color=ARROW_COLOR_PURPLE
                            )
                            if 'sub_enemy_list' in mission.log.keys():
                                for i,sub_enemy_info in enumerate(mission.log['sub_enemy_list']):
                                    dpg.draw_arrow((enemy_pos_1[0]-50,enemy_pos_1[1]-(i+1)*enemy_gap),
                                                (last_skill_frame_pos_0[0]+12,last_skill_frame_pos_0[1]),
                                                tag=f'last_skill_arrow_{sub_enemy_info[1]}',
                                                show=False,
                                                thickness=1,
                                                size=8,
                                                color=ARROW_COLOR_ORANGE
                                    )
                                    dpg.draw_arrow((enemy_pos_1[0]-50,enemy_pos_1[1]-(i+1)*enemy_gap),
                                                (next_skill_frame_pos_0[0]+12,next_skill_frame_pos_0[1]),
                                                tag=f'next_skill_arrow_{sub_enemy_info[1]}',
                                                show=False,
                                                thickness=3,
                                                size=10,
                                                color=ARROW_COLOR_PURPLE
                                    )

                        with dpg.group(parent='battle_operating_simulation') as temp_group:    # 左下技能备注显示和左上事件轴
                            next_event_time_pos_0 = (20,90)
                            next_event_period_pos_0 = (220,90)
                            next_event_note_pos_0 = (20,115)
                            last_event_time_pos_0 = (20,145)
                            last_event_period_pos_0 = (220,145)
                            last_event_note_pos_0 = (20,170)
                            next_skill_note_pos_0 = (20,525)
                            last_skill_note_pos_0 = (20,550)
                            dpg.add_text('距下个事件还有：N/A', tag='next_event_time', color=ARROW_COLOR_BLUE, pos=next_event_time_pos_0)
                            dpg.add_text('距上个事件已过：N/A', tag='last_event_time', color=ARROW_COLOR_ORANGE, pos=last_event_time_pos_0)
                            dpg.add_text('时间段：N/A', tag='next_event_period', color=ARROW_COLOR_BLUE, pos=next_event_period_pos_0)
                            dpg.add_text('时间段：N/A', tag='last_event_period', color=ARROW_COLOR_ORANGE, pos=last_event_period_pos_0)
                            dpg.add_text('事件说明：', tag='next_event_note', color=ARROW_COLOR_BLUE, pos=next_event_note_pos_0)
                            dpg.add_text('事件说明：', tag='last_event_note', color=ARROW_COLOR_ORANGE, pos=last_event_note_pos_0)
                            dpg.add_text('将释放技能备注：', tag='next_skill_note', color=ARROW_COLOR_BLUE, pos=next_skill_note_pos_0)
                            dpg.add_text('已释放技能备注：', tag='last_skill_note', color=ARROW_COLOR_ORANGE, pos=last_skill_note_pos_0)
                        dpg.bind_item_font(temp_group, cn_font_medium)
                                

                    # last_simulation_time = mission.mission_time
                    last_simulation_time = 0
                    last_cost_num = 0
                    last_skill_student_name = ''
                    next_skill_student_name = ''
                    last_skill_time = -1
                    next_skill_time = -1
                    then_skill_student_name_list = ['','','','']
                    last_skill_target = ''
                    next_skill_target = ''
                    def drawlist_running_handler():
                        nonlocal last_simulation_time
                        nonlocal last_cost_num
                        nonlocal last_skill_student_name
                        nonlocal next_skill_student_name
                        nonlocal last_skill_time
                        nonlocal next_skill_time
                        nonlocal then_skill_student_name_list
                        nonlocal last_skill_target
                        nonlocal next_skill_target
                        current_simulation_time = dpg.get_value('simulation_time')
                        if current_simulation_time==last_simulation_time:
                            return
                        last_simulation_time = current_simulation_time
                        dpg.set_value('up_right_time_text', second_to_minsec(current_simulation_time)+'00')
                        if dpg.does_item_exist('simulation_time_display'):
                            dpg.set_value('simulation_time_display', second_to_minsec(current_simulation_time)+' / '+second_to_minsec(mission.mission_time))
                        
                        # cost显示部分
                        if current_simulation_time>0:
                            current_cost = round(table_cost_list[int((mission.mission_time-current_simulation_time)*30)],1)
                        else:
                            current_cost = round(table_cost_list[-1],1)
                        if current_cost>=0:
                            if last_cost_num!=int(current_cost):
                                dpg.hide_item(f'cost_num_{last_cost_num}')
                                dpg.show_item(f'cost_num_{int(current_cost)}')
                                last_cost_num = int(current_cost)
                            if not is_udb:
                                dpg.apply_transform(bar_mask, dpg.create_translation_matrix([22*int(current_cost)+20*(current_cost%1)-218+1-int(current_cost%1==0)*2, 0]))    # 22*整数格+20*小数格占比-218偏移+1修正-2恰好为整数时左平移
                            else:
                                dpg.apply_transform(bar_mask, dpg.create_translation_matrix([15*int(current_cost)+13*(current_cost%1)-298+1-int(current_cost%1==0)*2, 0]))
                        else:    # 显示“费用超支”提示
                            current_cost = -1
                            if last_cost_num!=int(current_cost):
                                dpg.hide_item(f'cost_num_{last_cost_num}')
                                dpg.show_item(f'cost_num_{int(current_cost)}')
                                last_cost_num = int(current_cost)
                            if not is_udb:
                                dpg.apply_transform(bar_mask, dpg.create_translation_matrix([-218+1-1*2, 0]))    # 22*整数格+20*小数格占比-218偏移+1修正-2恰好为整数时左平移
                            else:
                                dpg.apply_transform(bar_mask, dpg.create_translation_matrix([-298+1-1*2, 0]))


                        # 技能队列部分
                        last_skill_index = -1
                        next_skill_index = 0
                        for i,ex_time in enumerate(mission.global_ex_time_list):
                            if ex_time>=current_simulation_time:
                                last_skill_index = i
                                next_skill_index = i+1
                            else:
                                break
                        if next_skill_index>=len(mission.global_ex_time_list):
                            next_skill_index = -1
                        
                        if last_skill_index>=0:
                            skill_time, name, target_name, start_time, end_time, skill_cost, skill_type, note = mission.global_ex_timeline[last_skill_index]
                            dpg.set_value('last_skill_text', f'已释放 {round(skill_time-current_simulation_time,1)}s')
                            dpg.set_value('last_skill_note', f'已释放技能备注：{note}')
                            if name!=last_skill_student_name or skill_time!=last_skill_time:
                                if last_skill_student_name:
                                    dpg.hide_item(f'last_skill_{last_skill_student_name}_rectangle')
                                    dpg.hide_item(f'last_skill_{last_skill_student_name}_text')
                                    dpg.hide_item(f'last_skill_{last_skill_student_name}_image')
                                    dpg.hide_item(f'last_skill_student_frame_{last_skill_student_name}')
                                    if dpg.does_item_exist(f'last_skill_arrow_{last_skill_target}'):
                                        dpg.hide_item(f'last_skill_arrow_{last_skill_target}')
                                dpg.show_item(f'last_skill_{name}_rectangle')
                                dpg.show_item(f'last_skill_{name}_text')
                                dpg.show_item(f'last_skill_{name}_image')
                                dpg.show_item(f'last_skill_student_frame_{name}')
                                if name!=target_name and dpg.does_item_exist(f'last_skill_arrow_{target_name}'):
                                    dpg.show_item(f'last_skill_arrow_{target_name}')
                                last_skill_student_name = name
                                last_skill_target = target_name
                                last_skill_time = skill_time
                        else:
                            dpg.set_value('last_skill_text', 'N/A')
                            dpg.set_value('last_skill_note', '已释放技能备注：')
                            if last_skill_student_name:
                                dpg.hide_item(f'last_skill_{last_skill_student_name}_rectangle')
                                dpg.hide_item(f'last_skill_{last_skill_student_name}_text')
                                dpg.hide_item(f'last_skill_{last_skill_student_name}_image')
                                dpg.hide_item(f'last_skill_student_frame_{last_skill_student_name}')
                                if dpg.does_item_exist(f'last_skill_arrow_{last_skill_target}'):
                                    dpg.hide_item(f'last_skill_arrow_{last_skill_target}')
                            last_skill_student_name = ''
                            last_skill_target = ''
                            last_skill_time = -1

                        if next_skill_index>=0:
                            skill_time, name, target_name, start_time, end_time, skill_cost, skill_type, note = mission.global_ex_timeline[next_skill_index]
                            dpg.set_value('next_skill_text', f'将释放 {round(current_simulation_time-skill_time,1)}s')
                            dpg.set_value('next_skill_note', f'将释放技能备注：{note}')
                            if name!=next_skill_student_name or skill_time!=next_skill_time:
                                if next_skill_student_name:
                                    dpg.hide_item(f'next_skill_{next_skill_student_name}_rectangle')
                                    dpg.hide_item(f'next_skill_{next_skill_student_name}_text')
                                    dpg.hide_item(f'next_skill_{next_skill_student_name}_image')
                                    dpg.hide_item(f'next_skill_student_frame_{next_skill_student_name}')
                                    if dpg.does_item_exist(f'next_skill_arrow_{next_skill_target}'):
                                        dpg.hide_item(f'next_skill_arrow_{next_skill_target}')
                                dpg.show_item(f'next_skill_{name}_rectangle')
                                dpg.show_item(f'next_skill_{name}_text')
                                dpg.show_item(f'next_skill_{name}_image')
                                dpg.show_item(f'next_skill_student_frame_{name}')
                                # print(f'hide:  next_skill_arrow_{next_skill_target}')    # 调试用
                                # print(f'show:  next_skill_arrow_{target_name}')
                                if name!=target_name and dpg.does_item_exist(f'next_skill_arrow_{target_name}'):
                                    dpg.show_item(f'next_skill_arrow_{target_name}')
                                next_skill_student_name = name
                                next_skill_target = target_name
                                next_skill_time = skill_time
                        else:
                            dpg.set_value('next_skill_text', 'N/A')
                            dpg.set_value('next_skill_note', '将释放技能备注：')
                            if next_skill_student_name:
                                dpg.hide_item(f'next_skill_{next_skill_student_name}_rectangle')
                                dpg.hide_item(f'next_skill_{next_skill_student_name}_text')
                                dpg.hide_item(f'next_skill_{next_skill_student_name}_image')
                                dpg.hide_item(f'next_skill_student_frame_{next_skill_student_name}')
                                if dpg.does_item_exist(f'next_skill_arrow_{next_skill_target}'):
                                    dpg.hide_item(f'next_skill_arrow_{next_skill_target}')
                            next_skill_student_name = ''
                            next_skill_target = ''
                            next_skill_time = -1
                        
                        for i in range(4):
                            if next_skill_index>=0 and len(mission.global_ex_time_list)-next_skill_index>=2+i:
                                skill_time, name, target_name, start_time, end_time, skill_cost, skill_type, note = mission.global_ex_timeline[next_skill_index+1+i]
                                dpg.set_value(f'then_{i}_skill_text', f'{round(current_simulation_time-skill_time,1)}s')
                                if name!=then_skill_student_name_list[i]:
                                    if then_skill_student_name_list[i]:
                                        dpg.hide_item(f'then_{i}_skill_{then_skill_student_name_list[i]}_rectangle')
                                        dpg.hide_item(f'then_{i}_skill_{then_skill_student_name_list[i]}_text')
                                        dpg.hide_item(f'then_{i}_skill_{then_skill_student_name_list[i]}_image')
                                    dpg.show_item(f'then_{i}_skill_{name}_rectangle')
                                    dpg.show_item(f'then_{i}_skill_{name}_text')
                                    dpg.show_item(f'then_{i}_skill_{name}_image')
                                    then_skill_student_name_list[i] = name
                            else:
                                dpg.set_value(f'then_{i}_skill_text', 'N/A')
                                if then_skill_student_name_list[i]:
                                    dpg.hide_item(f'then_{i}_skill_{then_skill_student_name_list[i]}_rectangle')
                                    dpg.hide_item(f'then_{i}_skill_{then_skill_student_name_list[i]}_text')
                                    dpg.hide_item(f'then_{i}_skill_{then_skill_student_name_list[i]}_image')
                                then_skill_student_name_list[i] = ''
                                

                        # 中部学生距下次技能时间显示
                        for sst in mission.student_skill_timelines:
                            student_display_name = sst.student.display_name
                            student_ex_time_list = list(sst.ex_timeline.keys())
                            student_ex_time_list.sort(reverse=True)
                            next_skill_index = 0
                            for i,ex_time in enumerate(student_ex_time_list):
                                if ex_time>current_simulation_time:
                                    next_skill_index = i+1
                                else:
                                    break
                            if next_skill_index>=len(student_ex_time_list):
                                dpg.set_value(f'central_next_skill_time_text_{student_display_name}', 'N/A')
                            else:
                                dpg.set_value(f'central_next_skill_time_text_{student_display_name}', f'距下次 {round(current_simulation_time-student_ex_time_list[next_skill_index],1)}s')


                        # 技能备注部分
                        last_event_index = -1
                        next_event_index = 0
                        for i,event_info in enumerate(mission.enemy.event_timeline):
                            event_start_time, event_end_time, note = event_info
                            if event_start_time>=current_simulation_time:
                                last_event_index = i
                                next_event_index = i+1
                            else:
                                break
                        if next_event_index>=len(mission.enemy.event_timeline):
                            next_event_index = -1

                        if last_event_index>=0:
                            event_start_time, event_end_time, note =  mission.enemy.event_timeline[last_event_index]
                            if current_simulation_time>event_end_time:
                                dpg.set_value('last_event_time', f'事件进行中，距结束：{round(current_simulation_time-event_end_time,1)}s')
                            else:
                                dpg.set_value('last_event_time', f'距上个事件已过：{round(event_end_time-current_simulation_time,1)}s')
                            dpg.set_value('last_event_period', f'时间段：{second_to_minsec(event_start_time)}-{second_to_minsec(event_end_time)}')
                            dpg.set_value('last_event_note', f'事件说明：{note}')
                        else:
                            dpg.set_value('last_event_time', '距上个事件已过：N/A')
                            dpg.set_value('last_event_period', '时间段：N/A')
                            dpg.set_value('last_event_note', '事件说明：')

                        if next_event_index>=0:
                            event_start_time, event_end_time, note =  mission.enemy.event_timeline[next_event_index]
                            dpg.set_value('next_event_time', f'距下个事件还有：{round(current_simulation_time-event_start_time,1)}s')
                            dpg.set_value('next_event_period', f'时间段：{second_to_minsec(event_start_time)}-{second_to_minsec(event_end_time)}')
                            dpg.set_value('next_event_note', f'事件说明：{note}')
                        else:
                            dpg.set_value('next_event_time', '距下个事件还有：N/A')
                            dpg.set_value('next_event_period', '时间段：N/A')
                            dpg.set_value('next_event_note', '事件说明：')
                    
                    with dpg.item_handler_registry():
                        dpg.add_item_visible_handler(callback=drawlist_running_handler)
                    dpg.bind_item_handler_registry("simulation_drawlist", dpg.last_root())


                    last_frame_system_time = time.time()
                    time_remainder = 0
                    def simulation_time_running_handler(sender, app_data):
                        nonlocal last_frame_system_time
                        nonlocal time_remainder
                        current_frame_system_time = time.time()
                        if not dpg.get_value('simulation_play'):
                            last_frame_system_time = current_frame_system_time
                            dpg.bind_item_theme('simulation_play_button', 'simulation_theme')
                            dpg.bind_item_theme('simulation_pause_button', 'simulation_active_theme')
                            return
                        dpg.bind_item_theme('simulation_play_button', 'simulation_active_theme')
                        dpg.bind_item_theme('simulation_pause_button', 'simulation_theme')
                        simulation_speed = dpg.get_value('simulation_speed')
                        current_simulation_time = dpg.get_value('simulation_time')
                        slider_time_unit = 0.1/simulation_speed
                        if current_simulation_time>0:
                            time_remainder += current_frame_system_time-last_frame_system_time
                            n = int(time_remainder/slider_time_unit)
                            time_remainder -= n*slider_time_unit
                            simulation_time = max(round(current_simulation_time-n*0.1,1),0)
                            dpg.set_value('simulation_time', simulation_time)
                        else:
                            dpg.set_value('simulation_play', False)
                        last_frame_system_time = current_frame_system_time

                    dpg.set_value('simulation_time', mission.mission_time)
                    dpg.set_value('simulation_play', False)
                    temp_slider = dpg.add_slider_float(parent='battle_operating_simulation', min_value=mission.mission_time, max_value=0, format='%.1f', default_value=mission.mission_time, width=800, height=20, source='simulation_time')
                    with dpg.item_handler_registry():
                        dpg.add_item_visible_handler(callback=simulation_time_running_handler)
                    dpg.bind_item_handler_registry(temp_slider, dpg.last_root())
                    with dpg.group(horizontal=True):
                        dpg.add_slider_float(label='倍速', tag='simulation_speed', min_value=0.1, max_value=3, width=100, default_value=1.0, format='%.1f')
                        dpg.add_button(label='1x', width=30, callback= lambda: dpg.set_value('simulation_speed', 1.0))
                        dpg.add_button(label='2x', width=30, callback= lambda: dpg.set_value('simulation_speed', 2.0))
                        dpg.add_button(label='3x', width=30, callback= lambda: dpg.set_value('simulation_speed', 3.0))
                        dpg.add_button(label='5x', width=30, callback= lambda: dpg.set_value('simulation_speed', 5.0))
                        dpg.add_button(label='10x', width=30, callback= lambda: dpg.set_value('simulation_speed', 10.0))
                        dpg.add_spacer(width=35)
                        dpg.add_button(tag='simulation_play_button', arrow=True, direction=dpg.mvDir_Right, callback= lambda: dpg.set_value('simulation_play', True))
                        dpg.add_button(tag='simulation_pause_button', label='II', width=25, callback= lambda: dpg.set_value('simulation_play', False))
                        dpg.add_spacer(width=265)
                        dpg.add_text('', tag='simulation_time_display')
                    
                    # 运行一次绘制handler，配合“last_simulation_time = 0”代码实现初始化
                    drawlist_running_handler()

                    # 空格、方向键handler    临时加了鼠标滚轮handler
                    if not dpg.does_item_exist('simulation_input_handler'):

                        def key_press_handler_callback(sender, data):
                            if not dpg.does_item_exist("battle_operating_simulation"):
                                return
                            type=dpg.get_item_info(sender)["type"]
                            if data==dpg.mvKey_Spacebar and dpg.does_item_exist('simulation_play'):
                                dpg.set_value('simulation_play', not dpg.get_value('simulation_play'))
                            elif data==dpg.mvKey_Up and dpg.does_item_exist('simulation_speed'):
                                last_speed = round(dpg.get_value('simulation_speed'),1)
                                current_speed = 0
                                speed_list = [0.1, 0.2, 0.5, 1.0, 2.0, 3.0, 5.0, 10.0]
                                for speed in speed_list:
                                    if last_speed<speed:
                                        current_speed = speed
                                        break
                                if current_speed:
                                    dpg.set_value('simulation_speed', current_speed)
                            elif data==dpg.mvKey_Down and dpg.does_item_exist('simulation_speed'):
                                last_speed = round(dpg.get_value('simulation_speed'),1)
                                current_speed = 0
                                speed_list = [10.0, 5.0, 3.0, 2.0, 1.0, 0.5, 0.2, 0.1]
                                for speed in speed_list:
                                    if last_speed>speed:
                                        current_speed = speed
                                        break
                                if current_speed:
                                    dpg.set_value('simulation_speed', current_speed)
                            elif data==dpg.mvKey_Left and dpg.does_item_exist('simulation_time'):
                                last_time = round(dpg.get_value('simulation_time'),1)
                                current_time = min(last_time + 5, mission.mission_time)
                                dpg.set_value('simulation_time', current_time)
                            elif data==dpg.mvKey_Right and dpg.does_item_exist('simulation_time'):
                                last_time = round(dpg.get_value('simulation_time'),1)
                                current_time = max(last_time - 5, 0)
                                dpg.set_value('simulation_time', current_time)
                        def mouse_wheel_handler_callback(sender, data):
                            if not dpg.does_item_exist("battle_operating_simulation"):
                                return
                            type=dpg.get_item_info(sender)["type"]
                            if data==-1 and dpg.does_item_exist('simulation_time'):
                                last_time = round(dpg.get_value('simulation_time'),1)
                                current_time = max(last_time - 1, 0)
                                dpg.set_value('simulation_time', current_time)
                            elif data==1 and dpg.does_item_exist('simulation_time'):
                                last_time = round(dpg.get_value('simulation_time'),1)
                                current_time = min(last_time + 1, mission.mission_time)
                                dpg.set_value('simulation_time', current_time)

                        with dpg.handler_registry(show=True, tag="simulation_input_handler"):
                            dpg.add_key_press_handler(callback=key_press_handler_callback)
                            dpg.add_mouse_wheel_handler(callback=mouse_wheel_handler_callback)


                dpg.bind_item_theme("battle_operating_simulation", 'simulation_theme')



                #  ######     ##            ####      ##    ##  
                #  ##   ##    ##           ##  ##     ###   ##  
                #  ##   ##    ##           ##  ##     ####  ##  
                #  ######     ##          ##    ##    ## ## ##  
                #  ##         ##          ########    ##  ####  
                #  ##         ##          ##    ##    ##   ###  
                #  ##         ##          ##    ##    ##    ##  
                #  ##         ########    ##    ##    ##    ##  


            with dpg.group(horizontal=True):
                with dpg.group():
                    dpg.add_spacer(width=400)
                    dpg.add_text('学生编辑')
                    # dpg.add_text('作战计划')
                    dpg.bind_item_font(dpg.last_item(), cn_font_large)
                    # dpg.add_text('[?]')
                    # with dpg.tooltip(dpg.last_item()):
                    #     dpg.add_text("拖动NS,EX按钮至计划表内以设置技能")
                    #     dpg.add_text("费用设置和敌人事件设置同理")
                    #     dpg.add_text("右键点击计划表内的技能/事件按钮以取消")
                # dpg.bind_item_font(dpg.last_item(), cn_font_medium)
                    with dpg.group(horizontal=True):
                        dpg.add_spacer(width=15)
                        dpg.add_button(label='添加学生', width=80, height=30, callback=add_student_button_callback)
                        with dpg.file_dialog(label='选择学生文件（仅英文路径）', default_path='./student_files/', width=750, height=500, directory_selector=False, show=False, callback=student_file_selector_callback_2, tag="student_file_dialog_2"):
                            dpg.add_file_extension(".csv", color=(96, 160, 64, 255))
                        dpg.add_spacer(width=10)
                        dpg.add_button(label='清空学生', width=80, height=30, callback=clear_student_button_callback)
                        dpg.bind_item_theme(dpg.last_item(), 'reset_theme')
                        dpg.add_spacer(width=10)
                        dpg.add_button(label='导出学生至本地', width=130, height=30, callback=export_student_button_callback)
                        with dpg.tooltip(dpg.last_item()):
                            dpg.add_text("将当前作战计划内的学生导出至./student_files/export_当前时间/")
                        # dpg.add_spacer(width=20)
                        dpg.add_text('', tag='student_file_exported_text')
                with dpg.window(label="其他单位编辑面板", width=540, height=300, tag='sub_enemy_edit_window', pos=(300,200), show=False):
                    def sub_enemy_edit_window_add_sub_enemy_button_callback():
                        display_name = dpg.get_value('sub_enemy_edit_window_sub_enemy_name')
                        mission.add_sub_enemy(Enemy(display_name))
                        # sub_enemy_edit_window_refresh_sub_enemy_list()
                        refresh_battle_plan()
                    def sub_enemy_edit_window_clear_sub_enemy_button_callback():
                        mission.clear_sub_enemy()
                        # sub_enemy_edit_window_refresh_sub_enemy_list()
                        refresh_battle_plan()
                    def sub_enemy_edit_window_delete_sub_enemy_button_callback(sender):
                        display_name = dpg.get_item_user_data(sender)
                        mission.remove_sub_enemy(display_name)
                        # sub_enemy_edit_window_refresh_sub_enemy_list()
                        refresh_battle_plan()
                    def sub_enemy_edit_window_refresh_sub_enemy_list():
                        dpg.delete_item('sub_enemy_edit_window_sub_enemy_list', children_only=True)
                        for sub_enemy in mission.sub_enemies:
                            with dpg.group(horizontal=True, parent='sub_enemy_edit_window_sub_enemy_list'):
                                dpg.add_text('')
                                dpg.add_button(label='删除', small=True, user_data=sub_enemy.display_name, callback=sub_enemy_edit_window_delete_sub_enemy_button_callback)
                                dpg.bind_item_theme(dpg.last_item(), 'delete_theme')
                                dpg.add_spacer(width=10)
                                dpg.add_text(sub_enemy.display_name)
                    with dpg.group(horizontal=True):
                        with dpg.group():
                            dpg.add_text('添加单位')
                            with dpg.group(horizontal=True, horizontal_spacing=0):
                                dpg.add_text('单位名称：')
                                dpg.add_input_text(label='', tag='sub_enemy_edit_window_sub_enemy_name', width=150)
                                dpg.add_spacer(width=10)
                                dpg.add_button(label="添加", width=50, callback=sub_enemy_edit_window_add_sub_enemy_button_callback)
                            dpg.add_button(label='清空单位', width=80, height=30, callback=sub_enemy_edit_window_clear_sub_enemy_button_callback)
                            dpg.bind_item_theme(dpg.last_item(), 'reset_theme')
                        dpg.add_spacer(width=10)
                        with dpg.group():
                            dpg.add_text('单位列表')
                            dpg.add_group(tag='sub_enemy_edit_window_sub_enemy_list')
                            sub_enemy_edit_window_refresh_sub_enemy_list()

                with dpg.group():
                    dpg.add_spacer(width=390)
                    dpg.add_text('其他单位编辑')
                    dpg.bind_item_font(dpg.last_item(), cn_font_large)
                    with dpg.group(horizontal=True):
                        dpg.add_spacer(width=15)
                        dpg.add_button(label='打开编辑面板', width=120, height=30, callback=lambda:dpg.show_item('sub_enemy_edit_window'))
                        dpg.add_spacer(width=10)
                        dpg.add_checkbox(label='显示其他单位受击和buff', tag='sub_enemy_edit_window_display_checkbox', callback=lambda:refresh_battle_plan(do_type='switch_sub_enemy_display'))
                with dpg.group():
                    dpg.add_text('实操辅助')
                    dpg.bind_item_font(dpg.last_item(), cn_font_large)
                    with dpg.group(horizontal=True):
                        dpg.add_spacer(width=15)
                        dpg.add_button(label="显示实操参考面板", width=150, height=30, callback=battle_operating_panel_callback)
                        dpg.add_spacer(width=10)
                        dpg.add_button(label="显示实操模拟", width=120, height=30, callback=battle_operating_simulation_callback)
            with dpg.group(tag='battle_plan_group'):
                def delete_student_callback(sender, app_data, user_data):
                    mission.remove_sst(user_data)
                    refresh_battle_plan()
                def student_reorder_drop_callback(sender, app_data):
                    target_display_name = dpg.get_item_user_data(sender)
                    source_display_name, operation = app_data
                    if operation=='switch':
                        mission.student_reorder_switch(source_display_name, target_display_name)
                        refresh_battle_plan()
                    else:
                        print('wrong command for student switch')
                def refresh_battle_plan(do_type=None):
                    def cost_button_callback(sender, app_data, user_data):
                        if user_data=='set_cost_timeline':
                            timepoint = dpg.get_value('cost_timeline_timepoint')
                            cost_speed = dpg.get_value('cost_timeline')
                            mission.set_cost_timeline(timepoint, cost_speed)
                            refresh_plan_table()
                        elif user_data=='set_cost_direct':
                            timepoint_min = dpg.get_value('cost_direct_timepoint_min')
                            timepoint_sec = dpg.get_value('cost_direct_timepoint_sec')
                            timepoint = timepoint_min*60 + timepoint_sec
                            timepoint = round(timepoint, 1)
                            cost_value = dpg.get_value('cost_direct')
                            mission.set_cost_direct(timepoint, cost_value)
                            refresh_plan_table()
                        else:
                            print('wrong cost command')
                    def cost_reset_callback(sender, app_data, user_data):
                        if user_data=='reset_cost_timeline':
                            mission.reset_cost_timeline()
                            refresh_plan_table()
                        elif user_data=='reset_cost_direct':
                            mission.reset_cost_direct()
                            refresh_plan_table()
                        else:
                            print('wrong cost command')
                    def cost_auto_set_callback():    # 不是最终的修改函数，而是弹出一个窗口显示预览并让用户确认是否应用，若确认，才会正式修改关卡时间轴
                        changed_flag = False
                        multi_id_warning_flag = False
                        mission_time = mission.mission_time
                        cost_init_delay = mission.cost_init_delay
                        cost_halo_student = ''
                        cost_halo_value = 0
                        cost_permanent_boost_list = []    # [(student_display_name, boost_value)]
                        cost_temporary_boost_list = []    # [(student_display_name, boost_value, start_time, end_time)]
                        cost_add_list = []    #[(student_display_name, add_value, start_time)]
                        # hoshino_swimsuit_list:list=[], himari_list:list=[], shiroko_swimsuit_list:list=[], kisaki_list:list=[], cherino_list:list=[], shun_list:list=[]
                        for student_info in mission.log['student_list']:
                            meet_count = 0
                            display_name:str = student_info[1]
                            ns_level = student_info[9]
                            ss_level = student_info[11]
                            ex_pre = student_info[26]
                            if (('水星' in display_name) or ('泳星' in display_name) or ('水叔' in display_name) or ('水大叔' in display_name) or ('星野（泳装）' in display_name)):
                                meet_count += 1
                                data_list = (0,360,378,396,468,486,504,576,594,612,684)
                                boost_value = data_list[ss_level]
                                
                                sst = mission.instance_dict[display_name]
                                temp_interval_list = []
                                for key,value in sst.ex_timeline.items():
                                    # time:[target, time-self.student.ex_pre, time-self.student.ex_pre-self.student.ex_dur, cost, skl_type, note]
                                    temp_interval_list.append((value[1], value[2]))
                                merged_interval_list = merge_intervals(temp_interval_list)
                                for start_time,end_time in merged_interval_list:
                                    cost_temporary_boost_list.append((display_name, boost_value, start_time, end_time))
                            if (('轮椅' in display_name) or ('阳葵' in display_name) or ('日鞠' in display_name)) and ('（' not in display_name):
                                meet_count += 1
                                data_list = (0.0, 0.106, 0.112, 0.117, 0.138, 0.144, 0.149, 0.170, 0.176, 0.181, 0.202)
                                halo_value = data_list[ss_level]
                                if cost_halo_value<halo_value:
                                    cost_halo_student = display_name
                                    cost_halo_value = halo_value
                            if (('水白' in display_name) or ('泳白' in display_name) or ('白子（泳装）' in display_name)):
                                meet_count += 1
                                data_list = (0.0, 0.106, 0.112, 0.117, 0.138, 0.144, 0.149, 0.170, 0.176, 0.181, 0.202)
                                halo_value = data_list[ss_level]
                                if cost_halo_value<halo_value:
                                    cost_halo_student = display_name
                                    cost_halo_value = halo_value
                            if (('ksk' in display_name.lower()) or ('妃姬' in display_name) or ('门主' in display_name) or ('妃咲' in display_name)) and ('（' not in display_name):
                                meet_count += 1
                                data_list = (0.0, 0.106, 0.112, 0.117, 0.138, 0.144, 0.149, 0.170, 0.176, 0.181, 0.202)
                                halo_value = data_list[ss_level]
                                if cost_halo_value<halo_value:
                                    cost_halo_student = display_name
                                    cost_halo_value = halo_value
                            if (('斯大' in display_name) or ('切里诺' in display_name)) and ('（' not in display_name):
                                meet_count += 1
                                data_list = (0, 269, 283, 296, 350, 363, 377, 431, 444, 457, 511)
                                boost_value = data_list[ss_level]
                                cost_permanent_boost_list.append((display_name, boost_value))
                            if (('舜' in display_name) or ('瞬' in display_name) or ('旬' in display_name)) and ('小' not in display_name) and ('（' not in display_name):
                                meet_count += 1
                                data_list = (0.0, 2.0, 2.1, 2.2, 2.6, 2.7, 2.8, 3.2, 3.3, 3.4, 3.8)
                                add_value = data_list[ns_level]
                                cost_add_list.append((display_name, add_value, mission_time-cost_init_delay))
                            if meet_count==1:
                                changed_flag = True
                            if meet_count>=2:
                                multi_id_warning_flag = True
                                multi_id_display_name = display_name
                                break
                        if multi_id_warning_flag:
                            with dpg.window(label="学生名识别失败：同学生多个关键词", width=540, height=130, modal=True, tag='cost_auto_set_confirm_window', pos=(300,200), on_close=lambda:dpg.delete_item('cost_auto_set_confirm_window')):
                                with dpg.group(horizontal=True):
                                    dpg.add_image('wtf_bro_img_texture')
                                    with dpg.group():
                                        dpg.add_text(f"学生 {multi_id_display_name} 的学生名中包含多个关键词，请修改其学生名后重试")
                                        dpg.add_text("（你是来找茬的吗（半恼")
                                        dpg.add_button(label="关闭", width=50, height=30, callback=lambda:dpg.delete_item('cost_auto_set_confirm_window'))
                        if changed_flag:
                            with dpg.window(label="费用轴设置预览", width=800, height=600, modal=True, tag='cost_auto_set_confirm_window', pos=(200,100), on_close=lambda:dpg.delete_item('cost_auto_set_confirm_window')):
                                def get_new_cost_timeline():
                                    mission_time = mission.mission_time
                                    cost_init_delay = mission.cost_init_delay
                                    student_num = len(mission.log['student_list'])
                                    time_checkpoint_set = set([mission_time, mission_time-cost_init_delay])
                                    cost_auto_set_command_list = []
                                    cost_auto_set_execute_data = []
                                    halo_value = 0
                                    permanent_boost_value = 0
                                    temporary_boost_data = []
                                    add_data = []

                                    for child in dpg.get_item_children('cost_auto_set_confirm_checkbox_panel', slot=1):
                                        if dpg.get_item_type(child)=='mvAppItemType::mvCheckbox':
                                            if dpg.get_value(child)==True:
                                                data = dpg.get_item_user_data(child)
                                                cost_auto_set_command_list.append(data)
                                                if data[0]=='halo':
                                                    if data[1]>halo_value:
                                                        halo_value = data[1]
                                                elif data[0]=='permanent_boost':
                                                    permanent_boost_value += data[1]
                                                elif data[0]=='temporary_boost':
                                                    time_checkpoint_set.add(data[2])
                                                    time_checkpoint_set.add(data[3])
                                                    temporary_boost_data.append(data[1:])
                                                elif data[0]=='add':
                                                    add_data.append(data[1:])
                                    cost_auto_set_command_list.sort()
                                    time_checkpoint_list = list(time_checkpoint_set)
                                    time_checkpoint_list.sort(reverse=True)
                                    for time_checkpoint in time_checkpoint_list:
                                        if time_checkpoint<=0:
                                            continue
                                        if time_checkpoint>mission_time-cost_init_delay:
                                            cost_auto_set_execute_data.append((time_checkpoint, 0, 'timeline'))
                                            continue
                                        temporary_boost_value = 0
                                        for data in temporary_boost_data:
                                            if time_checkpoint<=data[1] and time_checkpoint>data[2]:
                                                temporary_boost_value += data[0]
                                        cost_recovery_value = (700*student_num + permanent_boost_value + temporary_boost_value) * (1 + halo_value)
                                        cost_auto_set_execute_data.append((time_checkpoint, int(cost_recovery_value+0.5), 'timeline'))
                                    
                                    if add_data:
                                        for data in add_data:
                                            cost_auto_set_execute_data.append((data[1], data[0], 'direct'))
                                            
                                    dpg.delete_item('new_cost_timeline_preview')
                                    with dpg.group(tag='new_cost_timeline_preview', parent='cost_auto_set_confirm_timeline_panel'):
                                        dpg.add_text(f'\t时间点\t\t回费速度')
                                        for execute_data in cost_auto_set_execute_data:
                                            if execute_data[2]=='timeline':
                                                dpg.add_text(f'\t{second_to_minsec(execute_data[0])}\t\t{execute_data[1]}')
                                            elif execute_data[2]=='direct':
                                                dpg.add_spacer(height=10)
                                                dpg.add_text(f'\t{second_to_minsec(execute_data[0])}\t\t费用增加{execute_data[1]}')
                                            else:
                                                print('wrong cost_auto_set_execute_data')

                                    return cost_auto_set_execute_data

                                with dpg.group(horizontal=True):
                                    with dpg.group(tag='cost_auto_set_confirm_checkbox_panel'):
                                        dpg.add_text("以下学生技能会影响费用轴：（可手动取消勾选不需要的条目）")
                                        if cost_halo_student:
                                            dpg.add_spacer(height=5)
                                            dpg.add_text("回费速度光环", bullet=True)
                                            dpg.add_checkbox(label=f'{cost_halo_student}\t战斗开始后，提升全队回费速度{round(cost_halo_value*100,1)}%', user_data=('halo',cost_halo_value), default_value=True, callback=get_new_cost_timeline)
                                        if cost_permanent_boost_list:
                                            dpg.add_spacer(height=10)
                                            dpg.add_text("回费速度数值提升 - 全局覆盖", bullet=True)
                                            for item in cost_permanent_boost_list:
                                                dpg.add_checkbox(label=f'{item[0]}\t战斗开始后，回费速度数值提升{item[1]}', user_data=('permanent_boost',item[1]), default_value=True, callback=get_new_cost_timeline)
                                        if cost_temporary_boost_list:
                                            dpg.add_spacer(height=10)
                                            dpg.add_text("回费速度数值提升 - 技能期间", bullet=True)
                                            for item in cost_temporary_boost_list:
                                                dpg.add_checkbox(label=f'{item[0]}\t{second_to_minsec(item[2])}-{second_to_minsec(item[3])}期间，回费速度数值提升{item[1]}', user_data=('temporary_boost',item[1],item[2],item[3]), default_value=True, callback=get_new_cost_timeline)
                                        if cost_add_list:
                                            dpg.add_spacer(height=10)
                                            dpg.add_text("费用直接增加", bullet=True)
                                            for item in cost_add_list:
                                                dpg.add_checkbox(label=f'{item[0]}\t{second_to_minsec(item[2])}时，费用直接增加{item[1]}', user_data=('add',item[1],item[2]), default_value=True, callback=get_new_cost_timeline)
                                        time.sleep(0.01)
                                    dpg.add_spacer(width=20)
                                    with dpg.group():
                                        dpg.add_text("修改后的费用轴预览：")
                                        dpg.add_group(tag='cost_auto_set_confirm_timeline_panel')
                                        cost_auto_set_execute_data = get_new_cost_timeline()
                                        with dpg.group(horizontal=True):
                                            dpg.add_button(label='应用', width=50, height=30, callback=lambda:cost_auto_set_execute(cost_auto_set_execute_data))
                                            with dpg.tooltip(dpg.last_item()):
                                                dpg.add_text('会重置当前已有的费用轴', color=(255,96,96))
                                            dpg.add_spacer(width=10)
                                            dpg.add_button(label="取消", width=50, height=30, callback=lambda:dpg.delete_item('cost_auto_set_confirm_window'))
                                        
                        else:
                            with dpg.window(label="费用轴无修改", width=540, height=130, modal=True, tag='cost_auto_set_confirm_window', pos=(300,200), on_close=lambda:dpg.delete_item('cost_auto_set_confirm_window')):
                                with dpg.group(horizontal=True):
                                    dpg.add_image('wtf_bro_img_texture')
                                    with dpg.group():
                                        dpg.add_text("未识别到会对费用轴产生影响的学生，费用轴保持不变")
                                        dpg.add_button(label="关闭", width=50, height=30, callback=lambda:dpg.delete_item('cost_auto_set_confirm_window'))
                        # '星野（泳装）：水星、泳星、水叔、水大叔、星野（泳装）'
                        # '日鞠：轮椅、阳葵、日鞠'
                        # '白子（泳装）：水白、泳白、白子（泳装）'
                        # '妃咲：ksk、妃姬、门主、妃咲'
                        # '瞬：旬、舜、瞬；黑名单：小'
                    def cost_auto_set_execute(cost_auto_set_execute_data):
                        print(cost_auto_set_execute_data)
                        mission.reset_cost_timeline()
                        mission.reset_cost_direct()
                        for execute_data in cost_auto_set_execute_data:
                            if execute_data[2]=='timeline':
                                mission.set_cost_timeline(execute_data[0], execute_data[1])
                            elif execute_data[2]=='direct':
                                mission.set_cost_direct(execute_data[0], execute_data[1])
                            else:
                                print('wrong cost auto set command')
                        time.sleep(0.01)
                        dpg.delete_item('cost_auto_set_confirm_window')
                        refresh_plan_table()

                    def event_button_callback(sender, app_data):
                        event_start_time_min = dpg.get_value('event_start_time_min')
                        event_start_time_sec = dpg.get_value('event_start_time_sec')
                        event_start_time = event_start_time_min*60 + event_start_time_sec
                        event_start_time = round(event_start_time, 1)
                        # start_time = dpg.get_value('event_start_time')
                        event_end_time_min = dpg.get_value('event_end_time_min')
                        event_end_time_sec = dpg.get_value('event_end_time_sec')
                        event_end_time = event_end_time_min*60 + event_end_time_sec
                        event_end_time = round(event_end_time, 1)
                        # end_time = dpg.get_value('event_end_time')
                        note = dpg.get_value('event_note')
                        mission.add_enemy_event(max(event_end_time, event_start_time), min(event_end_time, event_start_time), note)
                        refresh_plan_table()
                    def event_reset_callback(sender, app_data):
                        mission.clear_enemy_event()
                        refresh_plan_table()
                    def clear_ns_callback(sender, app_data, user_data):
                        student_display_name = user_data
                        mission.clear_student_ns(student_display_name)
                        refresh_plan_table()
                    def clear_ex_callback(sender, app_data, user_data):
                        student_display_name = user_data
                        mission.clear_student_ex(student_display_name)
                        refresh_plan_table()
                    def cost_timeline_format_callback():
                        student_num_input = dpg.get_value('cost_timeline_student_num')
                        plus_input = dpg.get_value('cost_timeline_plus')
                        multiply_input = dpg.get_value('cost_timeline_multiply')
                        cost_recover_speed = (student_num_input*700 + plus_input) * (1 + round(multiply_input,1)/100)
                        cost_recover_speed = round(cost_recover_speed,0)
                        dpg.set_value('cost_timeline', cost_recover_speed)

                    sub_enemy_edit_window_refresh_sub_enemy_list()    # 顺便更新其他单位编辑窗口内容

                    is_udb = dpg.get_value('is_udb_checkbox')
                    # 若视窗已创建，则根据is_udb的情况，变更窗口大小
                    if dpg.is_viewport_ok():
                        current_viewport_width = dpg.get_viewport_width()
                        current_viewport_height = dpg.get_viewport_height()
                        if is_udb:
                            if current_viewport_width<1680:
                                dpg.set_viewport_width(1680)
                            if current_viewport_height<800:
                                dpg.set_viewport_height(800)
                        else:
                            if current_viewport_width<1200:
                                dpg.set_viewport_width(1200)
                            if current_viewport_height<800:
                                dpg.set_viewport_height(800)
                                
                    dpg.delete_item('battle_plan_group', children_only=True)

                    with dpg.group(horizontal=True, parent='battle_plan_group'):
                        dpg.add_text('控制台及作战计划')
                        dpg.bind_item_font(dpg.last_item(), cn_font_large)
                        dpg.add_text('[?]')
                        with dpg.tooltip(dpg.last_item()):
                            dpg.add_text("拖动NS,EX按钮至计划表内以设置技能")
                            dpg.add_text("费用设置和敌人事件设置同理")
                            dpg.add_text("右键点击计划表内的技能/事件按钮以取消")
                    def table_time_unit_select_callback():    # refresh_plan_table定义在后面，所以这里callback无法直接使用，必须提前声明
                        refresh_plan_table(do_type='unchange')
                    with dpg.group(horizontal=True, parent='battle_plan_group'):
                        with dpg.group(horizontal=True):
                            dpg.add_text('每格时间跨度(秒) [?]')
                            dpg.add_radio_button([0.1,0.2,0.5,1,2,5,10], label='单位时间长度(秒)', default_value=1, horizontal=True, callback=table_time_unit_select_callback, tag='table_time_unit')
                        with dpg.tooltip(dpg.last_container()):
                            dpg.add_text("摸轴时建议设为1秒或0.5秒，可应对绝大多数情况")
                            dpg.add_text("若需要目押等精细操作，可考虑设为0.2秒（性能下降，刷新较慢）")
                            dpg.add_text("出于实用性和本工具性能考虑，不建议设为0.1秒")
                        dpg.add_spacer(width=50)
                        dpg.add_button(label='撤 销', tag='undo_button', width=60, callback=mission_undo)
                        dpg.add_spacer(width=2)
                        dpg.add_button(label='重 做', tag='redo_button', width=60, callback=mission_redo)

                    with dpg.table(parent='battle_plan_group', header_row=False, borders_innerH=True, borders_outerH=True, borders_innerV=True, borders_outerV=True):
                        dpg.add_table_column(label="Header 1")
                        dpg.add_table_column(label="Header 2")
                        dpg.add_table_column(label="Header 3")
                        dpg.add_table_column(label="Header 4")
                        dpg.add_table_column(label="Header 5")
                        dpg.add_table_column(label="Header 6")
                        dpg.add_table_column(label="Header 7")
                        dpg.add_table_column(label="Header 8")
                        dpg.add_table_column(label="Header 9")
                        if is_udb:
                            dpg.add_table_column(label="Header 10")
                            dpg.add_table_column(label="Header 11")
                            dpg.add_table_column(label="Header 12")
                            dpg.add_table_column(label="Header 13")

                        with dpg.table_row():
                            with dpg.group():
                                with dpg.group(horizontal=True, horizontal_spacing=0):
                                    dpg.add_text('回费速度')
                                    dpg.add_spacer(width=10)
                                    dpg.add_button(label='重置', user_data='reset_cost_timeline', callback=cost_reset_callback)
                                    dpg.bind_item_theme(dpg.last_item(), 'reset_theme')
                                dpg.add_spacer(height=5)
                                # dpg.add_input_float(label='时间点', width=50, min_value=0, max_value=600, step=0, format='%.1f', tag='cost_timeline_timepoint')
                                # with dpg.tooltip(dpg.last_item()):
                                #     dpg.add_text('请转化为秒再输入（分秒分别输入在做了在做了')
                                # with dpg.group(horizontal=True, horizontal_spacing=0):
                                #     with dpg.group():
                                #         dpg.add_text('回费加算 +')
                                #         dpg.add_text('回费乘算 +')
                                #     with dpg.group():
                                #         dpg.add_input_int(width=40, default_value=0, min_value=0, max_value=10000, step=0, tag='cost_timeline_plus')
                                #         dpg.add_input_float(width=40, default_value=0, min_value=0, max_value=1000, step=0, format='%.1f', tag='cost_timeline_multiply')
                                #     with dpg.group():
                                #         dpg.add_text('')
                                #         dpg.add_text('%')
                                dpg.add_button(label='一键自动设置', callback=cost_auto_set_callback)
                                with dpg.tooltip(dpg.last_item()):
                                    dpg.add_text('一键识别学生名、技能等级、技能释放时间，自动设置费用轴')
                                    dpg.add_text('只要学生名中包含识别关键字，则识别为对应学生\n例如“水星野”包含“水星”故识别为星野（泳装）')
                                    # dpg.add_text('例如“水星野”包含“水星”故识别为星野（泳装）')
                                    dpg.add_text('设置完后请务必确认是否符合实际情况\n格里高利、赛特、霍德等战斗会改变回费速度，需要额外手动设置', color=(255,96,96))
                                    # dpg.add_text('格里高利、赛特、霍德等战斗会改变回费速度，需要额外手动设置', color=(255,96,96))
                                    dpg.add_spacer(height=5)
                                    dpg.add_text('目前支持的学生及其识别关键字：')
                                    dpg.add_text('星野（泳装）：水星、泳星、水叔、水大叔、星野（泳装）', bullet=True)
                                    dpg.add_text('日鞠：轮椅、阳葵、日鞠；黑名单：中文左括号', bullet=True)
                                    dpg.add_text('白子（泳装）：水白、泳白、白子（泳装）', bullet=True)
                                    dpg.add_text('妃咲：ksk、KSK、妃姬、门主、妃咲；黑名单：中文左括号', bullet=True)
                                    dpg.add_text('切里诺：斯大、切里诺；黑名单：中文左括号', bullet=True)
                                    dpg.add_text('        仅计算无其他红冬学生时的情况，若有，请不要使用本功能', color=(255,96,96))
                                    dpg.add_text('瞬：旬、舜、瞬；黑名单：小、中文左括号', bullet=True)
                                    dpg.add_text('注：若包含黑名单关键字，则不识别为该学生，用于区分同名换皮学生')
                                with dpg.group(horizontal=True, horizontal_spacing=0) as temp_group:
                                    dpg.add_text('  (')
                                    dpg.add_input_int(width=20, default_value=10 if is_udb else 6, min_value=0, max_value=10, step=0, tag='cost_timeline_student_num', callback=cost_timeline_format_callback)
                                    with dpg.tooltip(dpg.last_item()):
                                        dpg.add_text('场上学生人数')
                                    dpg.add_text('*700+')
                                    dpg.add_input_int(width=40, default_value=0, min_value=0, max_value=10000, step=0, tag='cost_timeline_plus', callback=cost_timeline_format_callback)
                                    with dpg.tooltip(dpg.last_item()):
                                        dpg.add_text('回费速率增加固定数值')
                                        dpg.add_text('例：满SS水星野增加684')
                                    dpg.add_text(')')
                                dpg.bind_item_theme(temp_group, "small_input_frame_theme")
                                # dpg.bind_item_font(temp_group, cn_font_small)
                                with dpg.group(horizontal=True, horizontal_spacing=0) as temp_group:
                                    dpg.add_text('*(1+')
                                    dpg.add_input_float(width=35, default_value=0, min_value=0, max_value=1000, step=0, format='%.1f', tag='cost_timeline_multiply', callback=cost_timeline_format_callback)
                                    with dpg.tooltip(dpg.last_item()):
                                        dpg.add_text('回费速率增加一定比率')
                                        dpg.add_text('例：满SS轮椅增加20.2%')
                                    dpg.add_text('%) = ')
                                dpg.bind_item_theme(temp_group, "small_input_frame_theme")
                                # dpg.bind_item_font(temp_group, cn_font_small)

                                with dpg.group(horizontal=True, horizontal_spacing=5):
                                    dpg.add_input_int(width=50, default_value=7000 if is_udb else 4200, min_value=0, max_value=100000, step=0, tag='cost_timeline')
                                    with dpg.tooltip(dpg.last_item()):
                                        dpg.add_text('也可以跳过计算，直接在这里输入')
                                    # dpg.add_button(label='确认', user_data='set_cost_timeline', callback=cost_button_callback)
                                    temp_button = dpg.add_button(label='拖动设置')
                                    with dpg.drag_payload(parent=dpg.last_item(), drag_data='set_cost_timeline', payload_type="cost"):
                                        dpg.add_input_int(label='回费速度', source='cost_timeline', width=50, step=0, enabled=False)
                                    with dpg.tooltip(temp_button):
                                        dpg.add_text('直接拖动至“时间与费用”列的费用数字上')

                            with dpg.group():
                                dpg.add_text('费用直接增减')
                                dpg.add_button(label='重置', user_data='reset_cost_direct', callback=cost_reset_callback)
                                dpg.bind_item_theme(dpg.last_item(), 'reset_theme')
                                dpg.add_spacer(height=5)
                                with dpg.group(horizontal=True, horizontal_spacing=0):
                                    dpg.add_input_int(width=15, min_value=0, max_value=10, step=0, tag='cost_direct_timepoint_min')
                                    dpg.add_text(':')
                                    dpg.add_input_float(label='时间点', width=40, min_value=0, max_value=60, step=0, format='%.1f', tag='cost_direct_timepoint_sec')
                                # with dpg.tooltip(dpg.last_item()):
                                #     dpg.add_text('请转化为秒再输入（分秒分别输入在做了在做了')
                                dpg.add_input_float(label='费用增减', width=50, min_value=-20, max_value=20, step=0, format='%.2f', tag='cost_direct')
                                with dpg.group(horizontal=True):
                                    dpg.add_button(label='确认', user_data='set_cost_direct', callback=cost_button_callback)
                                    temp_button = dpg.add_button(label='拖动设置')
                                    with dpg.drag_payload(parent=dpg.last_item(), drag_data='set_cost_direct', payload_type="cost"):
                                        dpg.add_input_float(label='费用增减', source='cost_direct', width=50, step=0, format='%.2f', enabled=False)
                                    with dpg.tooltip(temp_button):
                                        dpg.add_text('可以不设置时间点，直接拖动至“时间与费用”列')

                            with dpg.group():
                                with dpg.group(horizontal=True):
                                    dpg.add_text('关卡事件')
                                    dpg.add_button(label='清空', callback=event_reset_callback)
                                    dpg.bind_item_theme(dpg.last_item(), 'reset_theme')
                                dpg.add_spacer(height=5)
                                with dpg.group(horizontal=True, horizontal_spacing=0):
                                    dpg.add_input_int(width=15, min_value=0, max_value=10, step=0, tag='event_start_time_min')
                                    dpg.add_text(':')
                                    dpg.add_input_float(label='开始', width=35, min_value=0, max_value=60, step=0, format='%.1f', tag='event_start_time_sec')
                                # dpg.add_input_float(label='开始', width=50, min_value=0, max_value=600, step=0, format='%.1f', tag='event_start_time')
                                # with dpg.tooltip(dpg.last_item()):
                                #     dpg.add_text('请转化为秒再输入（分秒分别输入在做了在做了')
                                with dpg.group(horizontal=True, horizontal_spacing=0):
                                    dpg.add_input_int(width=15, min_value=0, max_value=10, step=0, tag='event_end_time_min')
                                    dpg.add_text(':')
                                    dpg.add_input_float(label='结束', width=35, min_value=0, max_value=60, step=0, format='%.1f', tag='event_end_time_sec')
                                    def event_time_start_end_sync():
                                        dpg.set_value('event_end_time_min', dpg.get_value('event_start_time_min'))
                                        dpg.set_value('event_end_time_sec', dpg.get_value('event_start_time_sec'))
                                    dpg.add_button(label='同步', callback=event_time_start_end_sync)
                                    with dpg.tooltip(dpg.last_item()):
                                        dpg.add_text('将开始时间复制到结束时间，设置瞬时事件')
                                # dpg.add_input_float(label='结束', width=50, min_value=0, max_value=600, step=0, format='%.1f', tag='event_end_time')
                                # with dpg.tooltip(dpg.last_item()):
                                #     dpg.add_text('请转化为秒再输入（分秒分别输入在做了在做了')
                                dpg.add_input_text(label='内容', tag='event_note')
                                dpg.add_button(label='确认', callback=event_button_callback)

                            # def open_color_picker(sender, app_data, user_data):
                            #     student_row, text_tag = user_data
                            #     with dpg.window(label="选择颜色", modal=True, no_close=True):
                            #         dpg.add_color_picker(
                            #             label="颜色选择器",
                            #             default_value=[1.0, 1.0, 1.0, 1.0],  # 默认颜色为白色
                            #             callback=lambda s, a, u: update_color(text_tag, a),  # 当颜色改变时更新颜色
                            #             user_data=student_row
                            #         )
                            #         dpg.add_button(label="确定", callback=lambda: dpg.delete_item(dpg.last_container()))

                            # # 更新颜色的函数
                            # def update_color(text_tag, color):
                            #     dpg.configure_item(text_tag, color=color)
                            for student_info in mission.log['student_list']:
                                with dpg.group(user_data=student_info[1], drop_callback=student_reorder_drop_callback, payload_type='student_reorder'):
                                    if dpg.does_alias_exist(student_info[1]+"_theme"):
                                        dpg.delete_item(student_info[1]+"_theme")
                                    with dpg.theme(tag=student_info[1]+"_theme"):
                                        with dpg.theme_component(dpg.mvButton):
                                            dpg.add_theme_color(dpg.mvThemeCol_Button, (student_info[3]*main_theme_multiplier,student_info[4]*main_theme_multiplier,student_info[5]*main_theme_multiplier))
                                            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (student_info[3]*main_theme_multiplier+32,student_info[4]*main_theme_multiplier+32,student_info[5]*main_theme_multiplier+32))
                                            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (student_info[3]*main_theme_multiplier+56,student_info[4]*main_theme_multiplier+56,student_info[5]*main_theme_multiplier+56))
                                            text_color = (255,255,255) if 0.299*student_info[3]+0.587*student_info[4]+0.114*student_info[5]<128 else (0,0,0)
                                            dpg.add_theme_color(dpg.mvThemeCol_Text, text_color)
                                            dpg.add_theme_style(dpg.mvStyleVar_FrameBorderSize, 0, category=dpg.mvThemeCat_Core)
                                            # dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 10)
                                    with dpg.group(horizontal=True, horizontal_spacing=0):
                                        temp_button = dpg.add_button(label='≡', small=True)
                                        dpg.bind_item_theme(dpg.last_item(), student_info[1]+"_theme")
                                        with dpg.drag_payload(parent=dpg.last_item(), drag_data=[student_info[1],'switch'], payload_type='student_reorder'):
                                            dpg.add_button(label=student_info[1])
                                            dpg.bind_item_theme(dpg.last_item(), student_info[1]+'_theme')
                                        with dpg.tooltip(temp_button):
                                            dpg.add_text('拖动以变更站位')
                                        dpg.add_text(student_info[1], color=(student_info[3],student_info[4],student_info[5]))
                                        with dpg.tooltip(dpg.last_item()):
                                            temp_student_info_8 = 'm' if student_info[9]==10 else student_info[9]
                                            temp_student_info_9 = 'm' if student_info[10]==10 else student_info[10]
                                            temp_student_info_10 = 'm' if student_info[11]==10 else student_info[11]

                                            if student_info[6]>=5:
                                                liandu_text_1 = f'等级:专{student_info[6]-4} {student_info[7]}级   技能:{student_info[8]}{temp_student_info_8}{temp_student_info_9}{temp_student_info_10}'
                                            else:
                                                liandu_text_1 = f'等级:{student_info[6]}星 {student_info[7]}级   技能:{student_info[8]}{temp_student_info_8}{temp_student_info_9}{temp_student_info_10}'
                                            if student_info[15]>0:
                                                liandu_text_2 = f'装备:{student_info[12]}{student_info[13]}{student_info[14]}   爱用品:{student_info[15]}   能力解放:{student_info[16]} {student_info[17]} {student_info[18]}'
                                            else:
                                                liandu_text_2 = f'装备:{student_info[12]}{student_info[13]}{student_info[14]}   能力解放:{student_info[16]} {student_info[17]} {student_info[18]}'
                                            liandu_text_3 = f'EX类型:{student_info[23]}  默认费用:{student_info[24]}  前摇:{student_info[25]}  持续时间:{student_info[26]}'
                                            liandu_text_4 = f'NS类型:{student_info[27]}  CD:{student_info[28]}  前摇:{student_info[29]}  持续时间:{student_info[30]}'
                                            dpg.add_text(f'学生:{student_info[1]}')
                                            dpg.add_text(liandu_text_1)
                                            dpg.add_text(liandu_text_2)
                                            dpg.add_text(liandu_text_3)
                                            dpg.add_text(liandu_text_4)
                                            if len(student_info)>=31:
                                                # liandu_text_5 = f'备注:{student_info[30]}'
                                                if student_info[31]!='':
                                                    dpg.add_text(student_info[31])

                                        dpg.add_spacer(width=5)
                                        dpg.add_button(label='删除', small=True, user_data=student_info[1], callback=delete_student_callback)
                                        dpg.bind_item_theme(dpg.last_item(), 'delete_theme')
                                    # text_tag = f"student_{i}"
                                    # dpg.add_text(student_info[1], tag=text_tag)
                                    # dpg.add_button(label='', width=20, height=20, user_data=(i, text_tag), callback=open_color_picker, tag=f"color_button_{i}")
                                    # dpg.add_color_edit((255, 255, 255, 255), label="颜色", width=200, tag=f"student_{i}_color_edit", no_alpha=True, no_inputs=True, user_data='')
                                    # dpg.add_spacer(height=5)
                                    with dpg.group(horizontal=True, horizontal_spacing=0):
                                        img_path = student_info[2]
                                        texture_name = img_path+'_34'
                                        if not dpg.does_alias_exist(texture_name):
                                            load_image_to_texture_registry(img_path, texture_name=texture_name, size=(34,34), crop=True, bg_color=student_info[3:6])
                                        dpg.add_image(texture_name)
                                        with dpg.tooltip(dpg.last_item()):
                                            dpg.add_text(f'学生:{student_info[1]}')
                                            dpg.add_text(liandu_text_1)
                                            dpg.add_text(liandu_text_2)
                                            dpg.add_text(liandu_text_3)
                                            dpg.add_text(liandu_text_4)
                                            if len(student_info)>=31:
                                                # liandu_text_5 = f'备注:{student_info[30]}'
                                                if student_info[31]!='':
                                                    dpg.add_text(student_info[31])
                                        dpg.add_spacer(width=30)
                                        with dpg.group():
                                            dpg.add_button(label='清空NS', width=50, height=15, user_data=student_info[1], callback=clear_ns_callback, small=True)
                                            dpg.bind_item_theme(dpg.last_item(), 'reset_theme')
                                            dpg.bind_item_font(dpg.last_item(), cn_font_small)
                                            dpg.add_button(label='清空EX', width=50, height=15, user_data=student_info[1], callback=clear_ex_callback, small=True)
                                            dpg.bind_item_theme(dpg.last_item(), 'reset_theme')
                                            dpg.bind_item_font(dpg.last_item(), cn_font_small)
                                    with dpg.group(horizontal=True, horizontal_spacing=0) as temp_group:
                                        temp_button = dpg.add_button(label='NS', width=27)
                                        dpg.bind_item_theme(dpg.last_item(), student_info[1]+"_theme")
                                        with dpg.drag_payload(parent=dpg.last_item(), drag_data=[student_info[1],'add_ns'], payload_type="skill"):
                                            dpg.add_button(label=student_info[1]+'NS', small=True)
                                            dpg.bind_item_theme(dpg.last_item(), student_info[1]+'_theme')
                                        with dpg.tooltip(temp_button):
                                            dpg.add_text('直接拖动至“当前EX”列（对，就是“当前EX”列）')
                                        dpg.add_spacer(width=4)
                                        temp_button = dpg.add_button(label='EX', width=27)
                                        dpg.bind_item_theme(dpg.last_item(), student_info[1]+"_theme")
                                        with dpg.drag_payload(parent=dpg.last_item(), drag_data=[student_info[1],'add_ex'], payload_type="skill"):
                                            dpg.add_button(label=student_info[1]+'EX', small=True)
                                            dpg.bind_item_theme(dpg.last_item(), student_info[1]+'_theme')
                                        with dpg.tooltip(temp_button):
                                            dpg.add_text('直接拖动至“当前EX”列')
                                        # dpg.add_spacer(width=2)
                                        dpg.add_input_int(width=15, min_value=0, max_value=20, step=0, min_clamped=True, max_clamped=True, default_value=student_info[24], tag=student_info[1]+'_ex_cost')
                                        dpg.add_text('费')
                                        dpg.add_spacer(width=3)
                                        with dpg.group():
                                            dpg.add_spacer(height=1)
                                            temp_button = dpg.add_button(label='50%', small=True)
                                            dpg.bind_item_theme(dpg.last_item(), student_info[1]+"_theme")
                                            dpg.bind_item_font(dpg.last_item(), cn_font_mini)
                                            with dpg.drag_payload(parent=dpg.last_item(), drag_data=[student_info[1],'add_ex_half_cost'], payload_type="skill"):
                                                dpg.add_button(label=student_info[1]+'EX', small=True)
                                                dpg.bind_item_theme(dpg.last_item(), student_info[1]+'_theme')
                                            with dpg.tooltip(temp_button):
                                                dpg.add_text('EX费用减半')
                                                dpg.add_text('直接拖动至“当前EX”列')
                                            dpg.add_spacer(height=5)
                                            temp_button = dpg.add_button(label=' -1  ', small=True)
                                            dpg.bind_item_theme(dpg.last_item(), student_info[1]+"_theme")
                                            dpg.bind_item_font(dpg.last_item(), cn_font_mini)
                                            with dpg.drag_payload(parent=dpg.last_item(), drag_data=[student_info[1],'add_ex_reduced_cost'], payload_type="skill"):
                                                dpg.add_button(label=student_info[1]+'EX', small=True)
                                                dpg.bind_item_theme(dpg.last_item(), student_info[1]+'_theme')
                                            with dpg.tooltip(temp_button):
                                                dpg.add_text('EX费用-1')
                                                dpg.add_text('直接拖动至“当前EX”列')
                                        dpg.bind_item_theme(temp_group, 'no_vertical_spacing_theme')
                                    dpg.add_combo(['自身']+list(mission.instance_dict.keys()), label='目标', width=85, default_value='自身', tag=student_info[1]+'_target', height_mode=dpg.mvComboHeight_Large)
                                    with dpg.tooltip(dpg.last_item()):
                                        dpg.add_text('选择EX/NS的目标')
                                    dpg.add_input_text(label='备注', width=85, tag=student_info[1]+'_note')
                                    with dpg.tooltip(dpg.last_item()):
                                        dpg.add_text('设置EX/NS的备注')

                                
                                # ########      ####      ######     ##          ########    
                                #    ##        ##  ##     ##   ##    ##          ##          
                                #    ##        ##  ##     ##   ##    ##          ##          
                                #    ##       ##    ##    ######     ##          ######      
                                #    ##       ########    ##   ##    ##          ##          
                                #    ##       ##    ##    ##   ##    ##          ##          
                                #    ##       ##    ##    ##   ##    ##          ##          
                                #    ##       ##    ##    ######     ########    ########    


                    # def table_time_unit_select_callback(sender, app_data):
                    #     refresh_plan_table()
                    # with dpg.group(horizontal=True, parent='battle_plan_group'):
                    #     dpg.add_text('每格时间跨度(秒) [?]')
                    #     dpg.add_radio_button([0.1,0.2,0.5,1,2,5,10], label='单位时间长度(秒)', default_value=1, horizontal=True, callback=table_time_unit_select_callback, tag='table_time_unit')
                    # with dpg.tooltip(dpg.last_container()):
                    #     dpg.add_text("摸轴时建议设为1秒或0.5秒，可应对绝大多数情况")
                    #     dpg.add_text("若需要目押等精细操作，可考虑设为0.2秒")
                    #     dpg.add_text("出于实用性和本工具性能考虑，不建议设为0.1秒")
                    with dpg.table(tag='plan_table_header', parent='battle_plan_group', header_row=True, borders_innerH=True, borders_outerH=True, borders_innerV=True, borders_outerV=True):
                        # dpg.add_table_column(init_width_or_weight=0, width_fixed=True)
                        dpg.add_table_column(label="时间与费用")
                        dpg.add_table_column(label="当前EX(拖至此列)")
                        dpg.add_table_column(label="敌人&关卡事件")
                        for i, student_info in enumerate(mission.log['student_list']):
                            dpg.add_table_column(label=student_info[1])
                        dpg.add_table_column(label="", init_width_or_weight=13, width_fixed=True)
                    with dpg.child_window(label='作战计划表', tag='plan_table_window', parent='battle_plan_group', height=540):
                        dpg.add_group(horizontal=True, tag='plan_table_window_group', parent='plan_table_window', horizontal_spacing=0)
                        
                        table_cell_list_0 = []
                        table_cell_list_1 = []
                        def cost_drop_callback(sender, app_data):
                            mission_time = mission.mission_time
                            time_unit = float(dpg.get_value('table_time_unit'))
                            index = table_cell_list_0.index(sender)
                            time_point = round(mission_time-index*time_unit,1)
                            operation = app_data
                            if operation=='set_cost_timeline':
                                cost_speed = dpg.get_value('cost_timeline')
                                mission.set_cost_timeline(time_point, cost_speed)
                                refresh_plan_table()
                            elif operation=='set_cost_direct':
                                cost_value = dpg.get_value('cost_direct')
                                mission.set_cost_direct(time_point, cost_value)
                                refresh_plan_table()
                            else:
                                print('wrong cost command')
                        def skill_drop_callback(sender, app_data):
                            mission_time = mission.mission_time
                            time_unit = float(dpg.get_value('table_time_unit'))
                            index = table_cell_list_1.index(sender)
                            time_point = round(mission_time-index*time_unit,1)
                            # [student_info[1],'add_ex']
                            if app_data[1]=='set_ex':
                                ex_info = app_data[0]
                                student_display_name = ex_info[1]
                            else:
                                student_display_name = app_data[0]
                            operation = app_data[1]
                            if operation=='add_ns':
                                target = dpg.get_value(student_display_name+'_target')
                                target = student_display_name if target=='自身' else target
                                skl_type = mission.instance_dict[student_display_name].student.ns_type
                                target_instance = mission.instance_dict[target]
                                # if type(target_instance)==Student_Skill_Timeline and skl_type=='伤害':
                                #     target = mission.enemy.display_name                                 # 现在只有目标为学生、类型为伤害时才会强制将目标改为敌人
                                # target = mission.enemy.display_name if skl_type=='伤害' else target    # 新增支持其他敌人后，更新修正函数
                                note = dpg.get_value(student_display_name+'_note')
                                mission.add_student_ns(student_display_name, time_point, target, skl_type, note=note)
                                refresh_plan_table()
                            elif operation=='add_ex':
                                cost = dpg.get_value(student_display_name+'_ex_cost')
                                target = dpg.get_value(student_display_name+'_target')
                                target = student_display_name if target=='自身' else target
                                skl_type = mission.instance_dict[student_display_name].student.ex_type
                                target_instance = mission.instance_dict[target]
                                # if type(target_instance)==Student_Skill_Timeline and skl_type=='伤害':
                                #     target = mission.enemy.display_name                                 # 现在只有目标为学生、类型为伤害时才会强制将目标改为敌人
                                # target = mission.enemy.display_name if skl_type=='伤害' else target    # 新增支持其他敌人后，更新修正函数
                                note = dpg.get_value(student_display_name+'_note')
                                mission.add_student_ex(student_display_name, time_point, cost, target, skl_type, note=note)
                                refresh_plan_table()
                            elif operation=='add_ex_half_cost':
                                cost = int(dpg.get_value(student_display_name+'_ex_cost')/2+0.5)
                                target = dpg.get_value(student_display_name+'_target')
                                target = student_display_name if target=='自身' else target
                                skl_type = mission.instance_dict[student_display_name].student.ex_type
                                target_instance = mission.instance_dict[target]
                                # if type(target_instance)==Student_Skill_Timeline and skl_type=='伤害':
                                #     target = mission.enemy.display_name                                 # 现在只有目标为学生、类型为伤害时才会强制将目标改为敌人
                                # target = mission.enemy.display_name if skl_type=='伤害' else target    # 新增支持其他敌人后，更新修正函数
                                note = dpg.get_value(student_display_name+'_note')
                                mission.add_student_ex(student_display_name, time_point, cost, target, skl_type, note=note)
                                refresh_plan_table()
                            elif operation=='add_ex_reduced_cost':
                                cost = dpg.get_value(student_display_name+'_ex_cost')-1
                                target = dpg.get_value(student_display_name+'_target')
                                target = student_display_name if target=='自身' else target
                                skl_type = mission.instance_dict[student_display_name].student.ex_type
                                target_instance = mission.instance_dict[target]
                                # if type(target_instance)==Student_Skill_Timeline and skl_type=='伤害':
                                #     target = mission.enemy.display_name                                 # 现在只有目标为学生、类型为伤害时才会强制将目标改为敌人
                                # target = mission.enemy.display_name if skl_type=='伤害' else target    # 新增支持其他敌人后，更新修正函数
                                note = dpg.get_value(student_display_name+'_note')
                                mission.add_student_ex(student_display_name, time_point, cost, target, skl_type, note=note)
                                refresh_plan_table()
                            elif operation=='set_ex':
                                # [time, name, target_name, start_time, end_time, cost, skl_type, note]
                                last_time_point = ex_info[0]
                                cost = ex_info[5]
                                target = ex_info[2]
                                skl_type = ex_info[6]
                                note = ex_info[7]
                                mission.remove_student_ex(student_display_name, last_time_point)
                                mission.add_student_ex(student_display_name, time_point, cost, target, skl_type, note=note)
                                refresh_plan_table()
                            else:
                                print('wrong cost command')
                        def skill_button_right_click_callback(sender, app_data, user_data):
                            # [ex_info[0], ex_info[1], 'ex']
                            student_display_name = user_data[1]
                            time_point = user_data[0]
                            if user_data[2]=='ns':
                                mission.remove_student_ns(student_display_name, time_point)
                                refresh_plan_table()
                            elif user_data[2]=='ex':
                                mission.remove_student_ex(student_display_name, time_point)
                                refresh_plan_table()
                            else:
                                print('wrong skill remove command')
                        def skill_cost_input_change_callback(sender, app_data, user_data):
                            # [ex_info[0], ex_info[1], 'ex']
                            ex_info = user_data
                            student_display_name = ex_info[1]
                            time_point = ex_info[0]
                            new_cost = app_data
                            target = ex_info[2]
                            skl_type = ex_info[6]
                            note = ex_info[7]
                            mission.remove_student_ex(student_display_name, time_point)
                            mission.add_student_ex(student_display_name, time_point, new_cost, target, skl_type, note=note)
                            refresh_plan_table()
                        def event_button_right_click_callback(sender, app_data, user_data):
                            start_time = user_data[0]
                            end_time = user_data[1]
                            note = user_data[2]
                            mission.remove_enemy_event(start_time, end_time, note)
                            refresh_plan_table()

                        def refresh_plan_table(do_type=None):
                            # 若mission_log_undo_list为空，或者最后一个槽位和当前log不一样时，则append，并删除15格以外的槽
                            global mission_log_undo_list
                            global mission_log_redo_list
                            global mission_log_undo_buffer
                            if not do_type:
                                if not mission_log_undo_list:
                                    mission_log_undo_list.append(mission_log_undo_buffer)
                                    mission_log_undo_buffer = mission.log.copy()
                                    mission_log_redo_list = []
                                elif mission.log!=mission_log_undo_list[-1]:
                                    mission_log_undo_list.append(mission_log_undo_buffer)
                                    mission_log_undo_buffer = mission.log.copy()
                                    mission_log_redo_list = []
                                if len(mission_log_undo_list)>=16:
                                    mission_log_undo_list.pop(0)
                            dpg.disable_item('undo_button')
                            dpg.disable_item('redo_button')


                            code_start_time = time.time()
                            mission.refresh_global_ex_timeline()
                            mission.settle_buff()
                            mission_time = mission.mission_time
                            time_unit = float(dpg.get_value('table_time_unit'))
                            is_udb = dpg.get_value('is_udb_checkbox')
                            dpg.add_spacer(height=28*int(mission_time/time_unit), tag='temp_spacer', parent='plan_table_window_group')
                            dpg.delete_item('plan_table')
                            dpg.delete_item('in_table_buff_group')
                            dpg.delete_item('in_table_event_group')
                            dpg.delete_item('in_table_buff_group_test')
                            dpg.delete_item('in_table_event_group_test')

                            global table_cost_list
                            table_cost_list = []
                            current_cost = 0
                            last_cost_speed = 0
                            current_cost_timeline_index = 0
                            current_cost_direct_index = 0
                            current_cost_ex_index = 0
                            # cost_timeline和cost_direct是以dict形式记录的，这里将其转为list并排序
                            temp_cost_timeline_list = [[key, mission.cost_timeline[key]] for key in mission.cost_timeline.keys()]
                            temp_cost_timeline_list.sort(reverse=True)
                            temp_cost_direct_list = [[key, mission.cost_direct[key]] for key in mission.cost_direct.keys()]
                            temp_cost_direct_list.sort(reverse=True)
                            for i in range(int(mission_time*30)):
                                current_time = round(mission_time-i/30,3)
                                current_cost += (last_cost_speed/10000)/30
                                if current_cost_timeline_index<len(temp_cost_timeline_list):
                                    if current_time<=temp_cost_timeline_list[current_cost_timeline_index][0]:
                                        last_cost_speed = temp_cost_timeline_list[current_cost_timeline_index][1]
                                        current_cost_timeline_index+=1
                                if is_udb:
                                    current_cost = round(min(current_cost,20.0), 6)
                                else:
                                    current_cost = round(min(current_cost,10.0), 6)
                                if current_cost_direct_index<len(temp_cost_direct_list):
                                    if current_time<=temp_cost_direct_list[current_cost_direct_index][0]:
                                        current_cost += temp_cost_direct_list[current_cost_direct_index][1]
                                        current_cost_direct_index+=1
                                if current_cost_ex_index<len(mission.global_ex_timeline):
                                    if current_time<=mission.global_ex_timeline[current_cost_ex_index][0]:
                                        current_cost -= mission.global_ex_timeline[current_cost_ex_index][5]
                                        current_cost_ex_index+=1
                                if is_udb:
                                    current_cost = round(min(current_cost,20.0), 6)
                                else:
                                    current_cost = round(min(current_cost,10.0), 6)
                                table_cost_list.append(round(current_cost,2))
                            
                            global table_ex_list
                            table_ex_list = [[] for i in range(int(mission_time/time_unit))]
                            for index,ex_time in enumerate(mission.global_ex_time_list):
                                for i in range(int(mission_time/time_unit)):
                                    cell_time = round(mission_time-i*time_unit,1)
                                    if ex_time<=cell_time and ex_time>round(cell_time-time_unit,1):
                                        ex_info = mission.global_ex_timeline[index]
                                        table_ex_list[i].append(ex_info)
                                        # print(cell_time, cell_time-time_unit, ex_time, ex_info)    ##### debug用
                                        

                            # table_enemy_buff_list = [[] for i in range(int(mission_time/time_unit))]
                            # for buff in mission.enemy.buff_timeline:
                            #     for i in range(int(mission_time/time_unit)):
                            #         cell_time = round(mission_time-i*time_unit,1)
                            #         if (cell_time<=buff[0] and cell_time>buff[1]) or (cell_time>=buff[0] and cell_time-time_unit<buff[1]):
                            #             table_enemy_buff_list[i].append(buff)
                            # table_enemy_event_list = [[] for i in range(int(mission_time/time_unit))]
                            # for event in mission.enemy.event_timeline:
                            #     for i in range(int(mission_time/time_unit)):
                            #         cell_time = round(mission_time-i*time_unit,1)
                            #         if (cell_time<=event[0] and cell_time>event[1]) or (cell_time>=event[0] and round(cell_time-time_unit,1)<event[0]):
                            #             table_enemy_event_list[i].append(event)
                            # table_enemy_damage_list = [[] for i in range(int(mission_time/time_unit))]
                            # for damage in mission.enemy.damage_timeline:
                            #     for i in range(int(mission_time/time_unit)):
                            #         cell_time = round(mission_time-i*time_unit,1)
                            #         if (cell_time<=damage[0] and cell_time>damage[1]) or (cell_time>=damage[0] and round(cell_time-time_unit,1)<damage[0]):
                            #             table_enemy_damage_list[i].append(damage)
                            
                            table_student_ex_dict = {}
                            for sst in mission.student_skill_timelines:
                                student_display_name = sst.student.display_name
                                table_student_ex_dict[student_display_name] = [[] for i in range(int(mission_time/time_unit))]
                                for key,value in sst.ex_timeline.items():
                                    # time:[target, time-self.student.ex_pre, time-self.student.ex_pre-self.student.ex_dur, cost, skl_type, note]
                                    for i in range(int(mission_time/time_unit)):
                                        cell_time = round(mission_time-i*time_unit,1)
                                        if (cell_time<=key and cell_time>key) or (cell_time>=key and round(cell_time-time_unit,1)<key):
                                            table_student_ex_dict[student_display_name][i].append([key]+value)
                            table_student_ns_dict = {}
                            for sst in mission.student_skill_timelines:
                                student_display_name = sst.student.display_name
                                table_student_ns_dict[student_display_name] = [[] for i in range(int(mission_time/time_unit))]
                                for key,value in sst.ns_timeline.items():
                                    # time:[target, time-self.student.ex_pre, time-self.student.ex_pre-self.student.ex_dur, cost, skl_type, note]
                                    for i in range(int(mission_time/time_unit)):
                                        cell_time = round(mission_time-i*time_unit,1)
                                        if (cell_time<=key and cell_time>key) or (cell_time>=key and round(cell_time-time_unit,1)<key):
                                            table_student_ns_dict[student_display_name][i].append([key]+value)

                            # table_student_buff_dict = {}
                            # for sst in mission.student_skill_timelines:
                            #     student_display_name = sst.student.display_name
                            #     table_student_buff_dict[student_display_name] = [[] for i in range(int(mission_time/time_unit))]
                            #     for buff in sst.buff_timeline:
                            #         # [buff_start_time, buff_end_time, buff_name, buff_source]
                            #         for i in range(int(mission_time/time_unit)):
                            #             cell_time = round(mission_time-i*time_unit,1)
                            #             if (cell_time<=buff[0] and cell_time>buff[1]) or (cell_time>=buff[0] and round(cell_time-time_unit,1)<buff[0]):
                            #                 table_student_buff_dict[student_display_name][i].append(buff)
                            
                            nonlocal table_cell_list_0
                            nonlocal table_cell_list_1
                            global column_1_height_container_list
                            global column_0_width_container
                            global column_1_width_container
                            global column_2_width_container
                            global column_3_width_container_list
                            table_cell_list_0 = []
                            table_cell_list_1 = []
                            # column_2_width_container = 'DUMMY'    # 配合后续的随帧刷新用，需保证该值一直不为0
                            with dpg.table(tag='plan_table', parent='plan_table_window_group', resizable=True, header_row=False, borders_innerH=True, borders_outerH=True, borders_innerV=True, borders_outerV=True, row_background=True, delay_search=False):
                                dpg.add_table_column(label="时间与费用")
                                dpg.add_table_column(label="当前EX")
                                dpg.add_table_column(label="敌人")
                                for student_info in mission.log['student_list']:
                                    dpg.add_table_column(label=student_info[1])
                                first_iter_flag = True
                                column_1_height_container_list = []
                                column_3_width_container_list = []
                                for i in range(int(mission_time/time_unit)):
                                    with dpg.table_row():
                                        cell_time = round(mission_time-i*time_unit,1)
                                        # for j in range(3+len(mission.log['student_list'])):
                                        for j in range(3+1):
                                            if j==0:
                                                with dpg.group(horizontal=True, payload_type='cost', drop_callback=cost_drop_callback):
                                                    if first_iter_flag:
                                                        column_0_width_container = dpg.last_container()
                                                    # table_cell_dict_0[dpg.last_container()] = f'{cell_time}_{j}'
                                                    table_cell_list_0.append(dpg.last_container())
                                                    # temp_minute = int((cell_time)/60)
                                                    # temp_second = (cell_time)%60
                                                    dpg.add_text(second_to_minsec(cell_time)+' |')
                                                    cell_cost = table_cost_list[int((mission_time-cell_time)*30)]
                                                    cost_timeline_flag = False
                                                    for cost_checkpoint in mission.cost_timeline.keys():
                                                        if cell_time>=cost_checkpoint and round(cell_time-time_unit,1)<cost_checkpoint:
                                                            cost_timeline_flag = True
                                                            break
                                                    if cost_timeline_flag:
                                                        dpg.add_text(cell_cost, color=(20,160,48))
                                                        with dpg.tooltip(dpg.last_item()):
                                                            dpg.add_text(f'当前回费速率为：{mission.cost_timeline[cost_checkpoint]}')
                                                    elif cell_cost>=20 or (cell_cost>=10 and not is_udb):
                                                        dpg.add_text(cell_cost, color=(224,160,0))
                                                    elif cell_cost<=0:
                                                        dpg.add_text(cell_cost, color=(255,0,0))
                                                    else:
                                                        dpg.add_text(cell_cost)
                                                    cost_direct_flag = False
                                                    for cost_checkpoint in mission.cost_direct.keys():
                                                        if cell_time>=cost_checkpoint and round(cell_time-time_unit,1)<cost_checkpoint:
                                                            cost_direct_flag = True
                                                            break
                                                    if cost_direct_flag:
                                                        if mission.cost_direct[cost_checkpoint]>=0:
                                                            dpg.add_text('+'+str(mission.cost_direct[cost_checkpoint]), color=(20,160,48))
                                                        else:
                                                            dpg.add_text(mission.cost_direct[cost_checkpoint], color=(20,160,48))
                                                    # dpg.add_spacer(width=115, height=0)
                                            elif j==1:
                                                with dpg.group(horizontal=False, payload_type='skill', drop_callback=skill_drop_callback):
                                                    column_1_height_container_list.append(dpg.last_container())
                                                    if first_iter_flag:
                                                        column_1_width_container = dpg.last_container()
                                                    table_cell_list_1.append(dpg.last_container())
                                                    content_flag = False

                                                    cell_ex_list = table_ex_list[i]
                                                    if cell_ex_list:
                                                        dpg.add_spacer()
                                                    for ex_info in cell_ex_list:
                                                        content_flag = True
                                                        with dpg.group(horizontal=True, horizontal_spacing=0):
                                                            img_path='placeholder_path'
                                                            for student_info in mission.log['student_list']:
                                                                if student_info[1]==ex_info[1]:
                                                                    img_path = student_info[2]
                                                                    break
                                                            texture_name = img_path+'_18'
                                                            if not dpg.does_alias_exist(texture_name):
                                                                load_image_to_texture_registry(img_path, texture_name=texture_name, size=(18,18), crop=True, bg_color=student_info[3:6])
                                                            dpg.add_image(texture_name)
                                                            temp_ex_button = dpg.add_button(label=ex_info[1]+'EX', small=True)
                                                            dpg.bind_item_theme(dpg.last_item(), ex_info[1]+'_theme')
                                                            with dpg.drag_payload(parent=dpg.last_item(), drag_data=[ex_info,'set_ex'], payload_type="skill"):
                                                                dpg.add_button(label=ex_info[1]+'EX', small=True)
                                                                dpg.bind_item_theme(dpg.last_item(), ex_info[1]+'_theme')
                                                            with dpg.item_handler_registry():
                                                                dpg.add_item_clicked_handler(1, user_data=[ex_info[0], ex_info[1], 'ex'], callback=skill_button_right_click_callback)
                                                            dpg.bind_item_handler_registry(temp_ex_button, dpg.last_root())
                                                            with dpg.tooltip(temp_ex_button):
                                                                # temp_minute = int((ex_info[0])/60)
                                                                # temp_second = round((ex_info[0])%60,1)
                                                                dpg.add_text(f"释放时间点：{second_to_minsec(ex_info[0])}")
                                                                # dpg.add_text(f'释放时间点：{ex_info[0]}')
                                                                dpg.add_text(f'费用：{ex_info[5]}')
                                                                dpg.add_text(f'学生：{ex_info[1]}')
                                                                dpg.add_text(f'目标：{ex_info[2]}')
                                                                dpg.add_text(f'实际生效时段：{second_to_minsec(ex_info[3],2)}-{second_to_minsec(ex_info[4],2)}')
                                                                dpg.add_text(f'类型：{ex_info[6]}')
                                                                dpg.add_text(f'备注：{ex_info[7]}')
                                                            dpg.add_input_int(width=15, min_value=0, max_value=20, step=0, min_clamped=True, max_clamped=True, default_value=ex_info[5], user_data=ex_info, callback=skill_cost_input_change_callback)
                                                            dpg.bind_item_theme(dpg.last_item(), "small_input_frame_theme")

                                                    if not content_flag:
                                                        dpg.add_spacer(width=115,height=21)
                                                        pass
                                                    else:
                                                        dpg.add_spacer(width=115, height=0)
                                            elif j==2:
                                                with dpg.group(horizontal=True, horizontal_spacing=0):
                                                    if first_iter_flag:
                                                        column_2_width_container = dpg.last_container()
                                                    content_flag = False

                                                    spacer_length = 13*4+2
                                                    # 此处原来为cell_buff_list相关代码，已用buff条相关代码代替，仅保留spacer_length计算

                                                    # cell_event_list = table_enemy_event_list[i]
                                                    # for event in cell_event_list:
                                                    #     content_flag = True
                                                    #     if spacer_length!=0:
                                                    #         dpg.add_spacer(width=spacer_length)
                                                    #     spacer_length = 0
                                                    #     temp_event_button = dpg.add_button(label=event[2][:4], small=True)
                                                    #     # dpg.bind_item_theme(dpg.last_item(), buff[3]+'_theme')
                                                    #     with dpg.tooltip(dpg.last_item()):
                                                    #         dpg.add_text(f'事件时间段：{second_to_minsec(event[0])}-{second_to_minsec(event[1])}')
                                                    #         dpg.add_text(f'事件：{event[2]}')
                                                    #     with dpg.item_handler_registry():
                                                    #         dpg.add_item_clicked_handler(1, user_data=event, callback=event_button_right_click_callback)
                                                    #     dpg.bind_item_handler_registry(temp_event_button, dpg.last_root())

                                                    # # with dpg.group(horizontal=True, horizontal_spacing=0):
                                                    # cell_damage_list = table_enemy_damage_list[i]
                                                    # for damage in cell_damage_list:
                                                    #     content_flag = True
                                                    #     if spacer_length!=0:
                                                    #         dpg.add_spacer(width=spacer_length)
                                                    #     spacer_length = 0
                                                    #     dpg.add_button(label='hit', small=True)
                                                    #     dpg.bind_item_theme(dpg.last_item(), damage[2][:-3]+'_theme')
                                                    #     with dpg.tooltip(dpg.last_item()):
                                                    #         dpg.add_text(f'受击时间段：{second_to_minsec(damage[0])}-{second_to_minsec(damage[1])}')
                                                    #         dpg.add_text(f'伤害来源：{damage[2]}')
                                                            
                                            else:
                                                for k,student_info in enumerate(mission.log['student_list']):
                                                    # 这里为了优化性能，故意少了一个group嵌套
                                                    # 使用spacer_length来记录：若本格有控件，则需要在控件前插入多长的空格
                                                    spacer_length = 0
                                                    with dpg.group(horizontal=True, horizontal_spacing=0):
                                                        if first_iter_flag:
                                                            column_3_width_container_list.append(dpg.last_container())
                                                        content_flag = False
                                                        cell_ex_list = table_student_ex_dict[student_info[1]][i]
                                                        if cell_ex_list:
                                                            content_flag = True
                                                            for ex in cell_ex_list:
                                                                temp_ex_button = dpg.add_button(label='EX', small=True, user_data=[ex[0], student_info[1]], callback=lambda s, a, u: print(f"clicked_handler: {s} '\t' {a} '\t' {u}"))
                                                                dpg.bind_item_theme(dpg.last_item(), student_info[1]+'_theme')
                                                                with dpg.item_handler_registry():
                                                                    dpg.add_item_clicked_handler(1, user_data=[ex[0], student_info[1], 'ex'], callback=skill_button_right_click_callback)
                                                                dpg.bind_item_handler_registry(temp_ex_button, dpg.last_root())
                                                                with dpg.tooltip(temp_ex_button):
                                                                    # [time, target, time-self.student.ex_pre, time-self.student.ex_pre-self.student.ex_dur, cost, skl_type, note]
                                                                    dpg.add_text(f'释放时间点：{second_to_minsec(ex[0])}')
                                                                    dpg.add_text(f'费用：{ex[4]}')
                                                                    if isinstance(ex[1], Student_Skill_Timeline):
                                                                        target_display_name = ex[1].student.display_name
                                                                    else:
                                                                        target_display_name = ex[1].display_name
                                                                    dpg.add_text(f'目标：{target_display_name}')
                                                                    dpg.add_text(f'EX生效时间段：{second_to_minsec(ex[2],2)}-{second_to_minsec(ex[3],2)}')
                                                                    dpg.add_text(f'技能类型：{ex[5]}')
                                                                    dpg.add_text(f'备注：{ex[6]}')
                                                                dpg.add_spacer(width=2)
                                                        else:    # 若当前格无EX，则空同样长度的空格
                                                            # dpg.add_spacer(width=25)
                                                            spacer_length += 27
                                                        cell_ns_list = table_student_ns_dict[student_info[1]][i]
                                                        if cell_ns_list:
                                                            content_flag = True
                                                            for ns in cell_ns_list:
                                                                if spacer_length!=0:
                                                                    dpg.add_spacer(width=spacer_length)
                                                                    spacer_length = 0
                                                                temp_ns_button = dpg.add_button(label='NS', small=True, user_data=[ns[0], student_info[1]], callback=lambda s, a, u: print(f"clicked_handler: {s} '\t' {a} '\t' {u}"))
                                                                dpg.bind_item_theme(dpg.last_item(), student_info[1]+'_theme')
                                                                with dpg.item_handler_registry():
                                                                    dpg.add_item_clicked_handler(1, user_data=[ns[0], student_info[1], 'ns'], callback=skill_button_right_click_callback)
                                                                dpg.bind_item_handler_registry(temp_ns_button, dpg.last_root())
                                                                with dpg.tooltip(temp_ns_button):
                                                                    # [time, target, time-self.student.ns_pre, time-self.student.ns_pre-self.student.ns_dur, skl_type, note]
                                                                    dpg.add_text(f'释放时间点：{second_to_minsec(ns[0])}')
                                                                    if isinstance(ns[1], Student_Skill_Timeline):
                                                                        target_display_name = ns[1].student.display_name
                                                                    else:
                                                                        target_display_name = ns[1].display_name
                                                                    dpg.add_text(f'目标：{target_display_name}')
                                                                    dpg.add_text(f'NS生效时间段：{second_to_minsec(ns[2],2)}-{second_to_minsec(ns[3],2)}')
                                                                    dpg.add_text(f'技能类型：{ns[4]}')
                                                                    dpg.add_text(f'备注：{ns[5]}')
                                                                dpg.add_spacer(width=2)
                                                        else:    # 若当前格无NS，则空同样长度的空格
                                                            # dpg.add_spacer(width=27)
                                                            spacer_length += 29
                                                            
                                    first_iter_flag = False                
                                
                            # buff统一在该级缩进处添加
                            time.sleep(0.01)
                            column_0_width = dpg.get_item_state(column_0_width_container)["content_region_avail"][0]
                            column_1_width = dpg.get_item_state(column_1_width_container)["content_region_avail"][0]
                            column_2_width = dpg.get_item_state(column_2_width_container)["content_region_avail"][0]
                            column_3_width_list = [dpg.get_item_state(i)["content_region_avail"][0] for i in column_3_width_container_list]
                            row_height_list = [dpg.get_item_height('plan_table_window')-dpg.get_item_state(i)["content_region_avail"][1] for i in column_1_height_container_list]
                            # print(row_height_list)
                            def buff_bar_pos_cal(column, in_column_index, start_time, end_time):
                                column_2_baseline = column_0_width + column_1_width + 13 + 9*2
                                column_3_baseline = column_2_baseline + column_2_width + 56 + 9
                                bar_width = 13    #内置1像素间隙
                                if column==2:
                                    pos_x = column_2_baseline + in_column_index*bar_width
                                else:
                                    pos_x = column_3_baseline + sum(column_3_width_list[:column-3]) + 9*(column-3) + in_column_index*bar_width
                                
                                # row_height_list = [550-dpg.get_item_state(i)["content_region_avail"][1] for i in column_1_height_container_list]
                                row_0_baseline = 16
                                row_head_gap = -2    # 修正每格buff条上沿到格子上沿距离
                                row_tail_gap = -13    # 修正每格buff条下沿到格子下沿距离
                                start_row = int((mission_time - start_time)/time_unit)
                                end_row = int((mission_time - end_time)/time_unit) + int((mission_time - end_time)%time_unit!=0)
                                if end_row==start_row:
                                    end_row += 1    #若buff过短导致end_row和start_row相同，则end_row+1。似乎是其他bug导致的，本来不应该有这个情况出现
                                start_bias = 0      # [start_row-1]有EX技能时，修正每格buff条上沿的偏移
                                end_bias = 0        # [end_row-1]有EX技能时，修正每格buff条下沿的偏移
                                try:
                                    if table_ex_list[start_row-1]:
                                        start_bias = -3
                                except:
                                    pass
                                try:
                                    if table_ex_list[end_row-1]:
                                        end_bias = -3
                                except:
                                    if table_ex_list[-1]:
                                        end_bias = -3
                                # pos_y = row_0_baseline + start_row*row_height
                                # bar_height = bar_unit_height + (end_row-start_row)*row_height
                                # pos_y = row_0_baseline + sum(row_height_list[:start_row])
                                # bar_height = bar_unit_height + sum(row_height_list[start_row:end_row])
                                if start_row==0:
                                    pos_y = row_0_baseline + start_bias
                                    bar_height = -pos_y + row_height_list[end_row-1] + row_tail_gap + end_bias
                                else:
                                    pos_y = row_height_list[start_row-1] + row_head_gap + start_bias
                                    try:
                                        bar_height = -pos_y + row_height_list[end_row-1] + row_tail_gap + end_bias
                                    except:
                                        bar_height = -pos_y + row_height_list[-1] + row_tail_gap + end_bias

                                return pos_x, pos_y, bar_width-1, bar_height
                            
                            # 测试buff条
                            # with dpg.group(tag='in_table_buff_group_test', parent='plan_table_window_group'):
                            #     for column in [2,3,4,5,6,7,8]:
                            #         # column = 4
                            #         in_column_index = 0
                            #         start_time = 230-column*4
                            #         end_time = 220-column*4
                            #         pos_x, pos_y, bar_width, bar_height = buff_bar_pos_cal(column, in_column_index, start_time, end_time)
                            #         dpg.add_button(width=bar_width, height=bar_height, pos=(pos_x,pos_y))
                            #         with dpg.tooltip(dpg.last_item()):
                            #             dpg.add_text(f'时间段：{second_to_minsec(start_time)}-{second_to_minsec(end_time)}')


                            sub_enemy_display_flag = dpg.get_value('sub_enemy_edit_window_display_checkbox')
                            with dpg.group(tag='in_table_buff_group', parent='plan_table_window_group'):
                                enemy_buff_register_dict = {}
                                enemy_buff_register_count = 0
                                merged_buff_timeline = []
                                if sub_enemy_display_flag:
                                    for buff_info in mission.enemy.buff_timeline:
                                        new_buff_info = buff_info+[mission.enemy.display_name]
                                        merged_buff_timeline.append(new_buff_info)
                                    for sub_enemy in mission.sub_enemies:
                                        for buff_info in sub_enemy.buff_timeline:
                                            new_buff_info = buff_info+[sub_enemy.display_name]
                                            merged_buff_timeline.append(new_buff_info)
                                    merged_buff_timeline.sort(reverse=True)
                                else:
                                    merged_buff_timeline = mission.enemy.buff_timeline
                                # for buff in mission.enemy.buff_timeline:
                                for buff in merged_buff_timeline:
                                    if buff[2] in enemy_buff_register_dict.keys():
                                        pass
                                    else:
                                        enemy_buff_register_dict[buff[2]] = enemy_buff_register_count
                                        enemy_buff_register_count += 1
                                    column = 2
                                    in_column_index = enemy_buff_register_dict[buff[2]]
                                    start_time = buff[0]
                                    end_time = buff[1]
                                    pos_x, pos_y, bar_width, bar_height = buff_bar_pos_cal(column, in_column_index, start_time, end_time)
                                    dpg.add_button(width=bar_width, height=bar_height, pos=(pos_x,pos_y), parent='in_table_buff_group', user_data=[column, in_column_index, start_time])
                                    dpg.bind_item_theme(dpg.last_item(), buff[3]+'_theme')
                                    with dpg.tooltip(dpg.last_item()):
                                        if sub_enemy_display_flag:
                                            dpg.add_text(f'单位：{buff[4]}')
                                        dpg.add_text(f'buff时间段：{second_to_minsec(buff[0],2)}-{second_to_minsec(buff[1],2)}')
                                        dpg.add_text(f'buff名：{buff[2]}')
                                        dpg.add_text(f'来源：{buff[3]}')
                                        
                                for k,student_info in enumerate(mission.log['student_list']):
                                    temp_student_buff_register_dict = {}
                                    temp_student_buff_register_count = 0
                                    for buff in mission.instance_dict[student_info[1]].buff_timeline:
                                        if buff[2] in temp_student_buff_register_dict.keys():
                                            pass
                                        else:
                                            temp_student_buff_register_dict[buff[2]] = temp_student_buff_register_count
                                            temp_student_buff_register_count += 1
                                        column = 3 + k
                                        in_column_index = temp_student_buff_register_dict[buff[2]]
                                        start_time = buff[0]
                                        end_time = buff[1]
                                        print(f'{buff[2]}:  {start_time}-{end_time}')
                                        pos_x, pos_y, bar_width, bar_height = buff_bar_pos_cal(column, in_column_index, start_time, end_time)
                                        dpg.add_button(width=bar_width, height=bar_height, pos=(pos_x,pos_y), parent='in_table_buff_group', user_data=[column, in_column_index, start_time])
                                        dpg.bind_item_theme(dpg.last_item(), buff[3]+'_theme')
                                        with dpg.tooltip(dpg.last_item()):
                                            dpg.add_text(f'buff时间段：{second_to_minsec(buff[0],2)}-{second_to_minsec(buff[1],2)}')
                                            dpg.add_text(f'buff名：{buff[2]}')
                                            dpg.add_text(f'来源：{buff[3]}')
                                            # dpg.add_text(f'{(pos_x, pos_y, bar_width, bar_height)}')    ##### debug用
                            
                            def event_bar_pos_cal(event_type, in_column_index, start_time, end_time):    # type为str，值可为'event', 'damage'
                                bar_width = 13    #内置1像素间隙
                                column_2_baseline = column_0_width + column_1_width + 13 + 2*9 + 3*bar_width
                                pos_x = column_2_baseline + in_column_index*bar_width
                                
                                # row_height_list = [550-dpg.get_item_state(i)["content_region_avail"][1] for i in column_1_height_container_list]
                                row_0_baseline = 16
                                row_head_gap = -2    # 修正每格buff条上沿到格子上沿距离
                                row_tail_gap = -13    # 修正每格buff条下沿到格子下沿距离
                                start_row = int((mission_time - start_time)/time_unit)
                                end_row = int((mission_time - end_time)/time_unit) + int((mission_time - end_time)%time_unit!=0)
                                if end_row==start_row:
                                    end_row += 1    #若buff过短导致end_row和start_row相同，则end_row+1。似乎是其他bug导致的，本来不应该有这个情况出现
                                start_bias = 0      # [start_row-1]有EX技能时，修正每格buff条上沿的偏移
                                end_bias = 0        # [end_row-1]有EX技能时，修正每格buff条下沿的偏移
                                try:
                                    if table_ex_list[start_row-1]:
                                        start_bias = -3
                                except:
                                    pass
                                try:
                                    if table_ex_list[end_row-1]:
                                        end_bias = -3
                                except:
                                    if table_ex_list[-1]:
                                        end_bias = -3
                                # pos_y = row_0_baseline + start_row*row_height
                                # bar_height = bar_unit_height + (end_row-start_row)*row_height
                                # pos_y = row_0_baseline + sum(row_height_list[:start_row])
                                # bar_height = bar_unit_height + sum(row_height_list[start_row:end_row])
                                if start_row==0:
                                    pos_y = row_0_baseline + start_bias
                                    bar_height = -pos_y + row_height_list[end_row-1] + row_tail_gap + end_bias
                                else:
                                    pos_y = row_height_list[start_row-1] + row_head_gap + start_bias
                                    try:
                                        bar_height = -pos_y + row_height_list[end_row-1] + row_tail_gap + end_bias
                                    except:
                                        bar_height = -pos_y + row_height_list[-1] + row_tail_gap + end_bias

                                return pos_x, pos_y, bar_width-1, bar_height

                            with dpg.group(tag='in_table_event_group', parent='plan_table_window_group'):
                                damage_register_dict = {}
                                damage_register_count = 0
                                merged_damage_timeline = []
                                if sub_enemy_display_flag:
                                    for damage_info in mission.enemy.damage_timeline:
                                        new_damage_info = damage_info+[mission.enemy.display_name]
                                        merged_damage_timeline.append(new_damage_info)
                                    for sub_enemy in mission.sub_enemies:
                                        for damage_info in sub_enemy.damage_timeline:
                                            new_damage_info = damage_info+[sub_enemy.display_name]
                                            merged_damage_timeline.append(new_damage_info)
                                    merged_damage_timeline.sort(reverse=True)
                                else:
                                    merged_damage_timeline = mission.enemy.damage_timeline
                                # for event in mission.enemy.damage_timeline:
                                for event in merged_damage_timeline:
                                    if event[2] in damage_register_dict.keys():
                                        pass
                                    else:
                                        damage_register_dict[event[2]] = damage_register_count
                                        damage_register_count += 1
                                    # [damage_start_time, damage_end_time, damage_source]
                                    # event_count += 1
                                    event_type = 'damage'
                                    in_column_index = 3 + damage_register_dict[event[2]]
                                    start_time = event[0]
                                    end_time = event[1]
                                    pos_x, pos_y, bar_width, bar_height = event_bar_pos_cal(event_type, in_column_index, start_time, end_time)
                                    bar_pos_y, bar_height = pos_y+18, bar_height-18
                                    if bar_height>=5:    # 事件条高度超过5时才显示
                                        dpg.add_button(width=bar_width, height=bar_height, pos=(pos_x,bar_pos_y), parent='in_table_event_group', user_data=[event_type, in_column_index, start_time])
                                        dpg.bind_item_theme(dpg.last_item(), event[2][:-3]+'_theme')
                                        with dpg.tooltip(dpg.last_item()):
                                            if sub_enemy_display_flag:
                                                dpg.add_text(f'单位：{event[3]}')
                                            dpg.add_text(f'受击时间段：{second_to_minsec(event[0],2)}-{second_to_minsec(event[1],2)}')
                                            dpg.add_text(f'来源：{event[2]}')
                                    dpg.add_button(label='hit', small=True, pos=(pos_x,pos_y), parent='in_table_event_group', user_data=[event_type, in_column_index, start_time])
                                    dpg.bind_item_theme(dpg.last_item(), event[2][:-3]+'_theme')
                                    with dpg.tooltip(dpg.last_item()):
                                        if sub_enemy_display_flag:
                                            dpg.add_text(f'单位：{event[3]}')
                                        dpg.add_text(f'受击时间段：{second_to_minsec(event[0],2)}-{second_to_minsec(event[1],2)}')
                                        dpg.add_text(f'来源：{event[2]}')
                                event_count = -1
                                for event in mission.enemy.event_timeline:
                                    # [event_start_time, event_end_time, note]
                                    event_count += 1
                                    event_type = 'event'
                                    in_column_index = event_count%3
                                    start_time = event[0]
                                    end_time = event[1]
                                    pos_x, pos_y, bar_width, bar_height = event_bar_pos_cal(event_type, in_column_index, start_time, end_time)
                                    bar_pos_y, bar_height = pos_y+18, bar_height-18
                                    if bar_height>=5:    # 事件条高度超过5时才显示
                                        dpg.add_button(width=bar_width, height=bar_height, pos=(pos_x,bar_pos_y), parent='in_table_event_group', user_data=[event_type, in_column_index, start_time])
                                        dpg.bind_item_theme(dpg.last_item(), 'grey_transparent_button_theme')
                                        with dpg.tooltip(dpg.last_item()):
                                            dpg.add_text(f'事件时间段：{second_to_minsec(event[0],2)}-{second_to_minsec(event[1],2)}')
                                            dpg.add_text(f'内容：{event[2]}')
                                    content = event[2] if len(event[2])<=4 else event[2][:4]
                                    temp_event_button = dpg.add_button(label=content, small=True, pos=(pos_x,pos_y), parent='in_table_event_group', user_data=[event_type, in_column_index, start_time])
                                    dpg.bind_item_theme(dpg.last_item(), 'grey_transparent_button_theme')
                                    with dpg.tooltip(dpg.last_item()):
                                        dpg.add_text(f'事件时间段：{second_to_minsec(event[0],2)}-{second_to_minsec(event[1],2)}')
                                        dpg.add_text(f'内容：{event[2]}')
                                        dpg.add_text('右键点击以删除该事件', color=(192,128,128))
                                    with dpg.item_handler_registry():
                                        dpg.add_item_clicked_handler(1, user_data=event, callback=event_button_right_click_callback)
                                    dpg.bind_item_handler_registry(temp_event_button, dpg.last_root())
                                    #     temp_event_button = dpg.add_button(label=event[2][:4], small=True)
                                    #     # dpg.bind_item_theme(dpg.last_item(), buff[3]+'_theme')
                                    #     with dpg.tooltip(dpg.last_item()):
                                    #         dpg.add_text(f'事件时间段：{second_to_minsec(event[0])}-{second_to_minsec(event[1])}')
                                    #         dpg.add_text(f'事件：{event[2]}')
                                    #     with dpg.item_handler_registry():
                                    #         dpg.add_item_clicked_handler(1, user_data=event, callback=event_button_right_click_callback)
                                    #     dpg.bind_item_handler_registry(temp_event_button, dpg.last_root())
                                        
                                

                            # print(table_cell_dict_0)

                            dpg.delete_item('temp_spacer')
                            code_end_time = time.time()
                            # print('checkpoint1\t',round(code_time_checkpoint_1 - code_start_time, 4))
                            print('execution time\t',round(code_end_time - code_start_time, 4))

                            # print('undo_list:', len(mission_log_undo_list))
                            # if mission_log_undo_list:
                            #     dpg.enable_item('undo_button')
                            # else:
                            #     dpg.disable_item('undo_button')
                            # print('redo_list:', len(mission_log_redo_list))
                            # if mission_log_redo_list:
                            #     dpg.enable_item('redo_button')
                            # else:
                            #     dpg.disable_item('redo_button')
                            dpg.enable_item('undo_button') if mission_log_undo_list else dpg.disable_item('undo_button')
                            dpg.enable_item('redo_button') if mission_log_redo_list else dpg.disable_item('redo_button')
                            switch_night_mode()

                        refresh_plan_table(do_type=do_type)

                refresh_battle_plan(do_type='init')
                
            

                #  ##    ##    ########    ##          ######    
                #  ##    ##    ##          ##          ##   ##   
                #  ##    ##    ##          ##          ##   ##   
                #  ########    ######      ##          ######    
                #  ##    ##    ##          ##          ##        
                #  ##    ##    ##          ##          ##        
                #  ##    ##    ##          ##          ##        
                #  ##    ##    ########    ########    ##     



        with dpg.tab(label="使用提示"):
            dpg.add_separator()
            dpg.add_spacer(height=5)
            dpg.add_text("一切以方便优先")
            dpg.bind_item_font(dpg.last_item(), cn_font_medium)
            dpg.add_separator()
            dpg.add_text("使用本工具(BATL.exe)时切记：一切以方便优先！视情况决定是否使用某个功能或填写某个字段", bullet=True)
            dpg.add_text("比如设置技能时可以不设置目标（即默认以自身为目标），只要看buff时自己能看懂（知道是某目标挂上了buff）就行", bullet=True)
            dpg.add_text("比如技能前摇等学生字段，除非对时间有严格要求，否则也可以留空不填", bullet=True)
            dpg.add_spacer(height=20)
            dpg.add_text("别高估自身手速")
            dpg.bind_item_font(dpg.last_item(), cn_font_medium)
            dpg.add_separator()
            dpg.add_text("一般用户（包括手机平板用户）建议每两个EX技能间隔都不短于0.5秒，以提升容错", bullet=True)
            dpg.add_text("制约解除决战中，考虑到操作难度和本工具性能，建议每两个EX技能间隔都不短于1秒，并将每格时间跨度设为不短于1s", bullet=True)
            dpg.add_text("一般情况下，在模拟器上手操不使用AUTO时，2个EX技能的释放间隔难以短于0.2秒，3个为0.5秒，4个为1.0秒（因为要等第四个EX显示出来后才能选定释放）", bullet=True)
            dpg.add_text("除非用户对手速有自信且有设置键位映射，否则不建议计划超过上述极限频率使用EX技能", bullet=True)
            dpg.add_text("若右下角备选EX技能顺序正确且无需手动选择目标，则可以使用AUTO自动释放EX技能，费用充足时每两个EX技能的释放间隔为固定0.066秒（2帧）", bullet=True)
            dpg.add_text("但这种情况不稳定，不建议在计划中使用", bullet=True)
            dpg.add_spacer(height=20)
            
        with dpg.tab(label="关于"):
            dpg.add_separator()
            dpg.add_spacer(height=5)
            with dpg.group(horizontal=True):
                dpg.add_text("若需反馈bug或有其他疑问与建议，请联系机管giga-35b  --> ")
                dpg.add_button(label='B站空间（私信）', callback=lambda:webbrowser.open('https://space.bilibili.com/15097920'))
                dpg.add_button(label='QQ', callback=lambda:dpg.set_value('qq_hint', "现在用QQ联系有点太早了，等到北京时间2041年11月21日凌晨3点57分38秒再说吧~" if not dpg.get_value('qq_hint') else ""))
                dpg.add_text('', tag='qq_hint')
            dpg.add_text('使用和分享时请遵守CC BY-NC-SA 4.0协议', bullet=True, color=(128,128,128))
            with dpg.tooltip(dpg.last_item()):
                dpg.add_text('您可以自由复制、散布、展示及演出本作品。', color=(128,128,128))
                dpg.add_text("您必须按照作者或授权人所指定的方式，保留其姓名标示。", color=(128,128,128))
                dpg.add_text('您不得为商业目的而使用本作品。', color=(128,128,128))
                dpg.add_text("若您改变、转变或改作本作品，仅在遵守与本著作相同的授权条款下，您才能散布由本作品产生的衍生作品。", color=(128,128,128))
            dpg.add_spacer(height=10)
            # dpg.add_text("开发日志")
            # dpg.bind_item_font(dpg.last_item(), cn_font_medium)
            dpg.add_separator()
            dpg.add_spacer(height=10)
            with dpg.collapsing_header(label='开发日志'):
                # dpg.bind_item_font(dpg.last_item(), cn_font_medium)
                content = [
                    ['2024.8.29', '/', '立项'],
                    ['2024.8.30', '/', '开始内核开发'],
                    ['2024.9.4', '/', '开始GUI开发'],
                    ['2024.9.6', '/', '完成GUI-学生编辑页面'],
                    ['2024.9.11', '/', '完成GUI-作战时间轴页面-外观'],
                    ['2024.9.12', '/', '完成GUI-作战时间轴页面-功能'],
                    ['2024.9.13', 'v0.5.0', '完成第一个功能测试版'],
                    ['2024.9.16', 'v0.6.0', '完成作战时间轴buff显示优化，极大幅提升性能（约5-10倍）'],
                    ['2024.9.17', 'v0.7.0', '新增人数上限提示、实操参考面板等功能，新增支持窗口缩放'],
                    ['2024.9.19', 'v0.8.0', '新增实操模拟等功能'],
                    ['2024.9.21', 'v0.8.2', 'bug修复&细节优化'],
                    ['2024.9.28', 'v0.9.0', '新增支持制约解除决战，外加技能费用编辑优化'],
                    ['2024.9.29', 'v0.9.1', '一堆bug修复和功能优化（特别鸣谢来BATL酒吧花式点炒饭的这个B 站用户：', ['@rkc018','https://space.bilibili.com/7727552','）']],
                    ['2024.10.1', '/', '2024.10.1-2024.10.7 国庆狠狠摸鱼'],
                    ['2024.10.8', 'v0.9.2', '现已支持中文路径，且恢复“打开文件夹”功能'],
                    ['2024.10.11', 'v0.9.3', 'ui界面优化，新增夜间模式主题'],
                    ['2024.10.17', 'v0.10.0', '新增学生头像相关功能，修改学生文件和关卡文件格式（旧版文件不再支持）'],
                    ['2024.10.18', 'v0.10.1', '新增从作战记录导出学生功能'],
                    ['2024.10.23', 'v0.10.2', '新增费用轴自动计算功能'],
                    ['2024.10.25', 'v0.10.3', '新增撤销与重做功能'],
                    ['2024.10.28', 'v0.10.4', '优化作战计划中的事件显示'],
                    ['2024.10.29', 'v0.10.5', '新增支持添加其他单位（如奶奶灯、拘束弹控制器等）'],
                    ['2024.11.1', '/', '2024.11.1-2024.11.3 很忙，在MHWS beta test里打放电纸飞机，什么事'],
                    ['2024.11.4', 'v0.10.6', '实操模拟箭头bug修复，事件位置bug修复，事件条显示优化'],
                ]
                dpg.add_text("      时间                 版本号       内容")
                with dpg.group(horizontal=True):
                    with dpg.group():
                        for string_list in content:
                            dpg.add_text(string_list[0], bullet=True)
                    dpg.add_spacer(width=9)
                    with dpg.group():
                        for string_list in content:
                            dpg.add_text(string_list[1])
                    dpg.add_spacer(width=9)
                    with dpg.group():
                        for string_list in content:
                            with dpg.group(horizontal=True):
                                dpg.add_text(string_list[2])
                                if len(string_list)>3:
                                    if isinstance(string_list[3], list):
                                        # dpg.add_text(string_list[2])
                                        dpg.add_button(label=string_list[3][0], small=True, callback=lambda:webbrowser.open(string_list[3][1]))
                                        dpg.add_text(string_list[3][2])
                                    # elif string_list[3]=='grey':
                                    #     dpg.add_text(string_list[2], color=(128,128,128))
                                    # else:
                                    #     dpg.add_text(string_list[2])

                                    

                # dpg.add_text("      时间               版本号\t     内容")
                # dpg.add_text("2024.08.29    /      \t        立项", bullet=True)
                # dpg.add_text("2024.08.30    v0.1.x \t     开始内核开发", bullet=True)
                # dpg.add_text("2024.09.04    v0.11.x\t    开始GUI开发", bullet=True)
                # dpg.add_text("2024.09.06    v0.2.x \t        完成GUI-学生编辑页面", bullet=True)
                # dpg.add_text("2024.09.11    v0.12.x\t        完成GUI-作战时间轴页面-外观", bullet=True)
                # dpg.add_text("2024.09.12    v0.22.x\t        完成GUI-作战时间轴页面-功能", bullet=True)
                # dpg.add_text("2024.09.13    v0.x.x        完成第一个功能测试版，版本号BATL_v0.5.0_beta", bullet=True)
                # dpg.add_text("2024.09.16    v0.x.x        完成作战时间轴buff显示优化，极大幅提升性能（约5-10倍），版本号BATL_v0.6.0_beta", bullet=True)
                # dpg.add_text("2024.09.17    v0.x.x        新增人数上限提示、实操参考面板等功能，新增支持窗口缩放，版本号BATL_v0.7.0_beta", bullet=True)
                # dpg.add_text("2024.09.19    v0.x.x        新增实操模拟等功能，版本号BATL_v0.8.0_beta", bullet=True)
                # dpg.add_text("2024.09.21    v0.x.x        bug修复&细节优化，版本号BATL_v0.8.2_beta", bullet=True)
                # dpg.add_text("2024.09.28    v0.x.x        新增支持制约解除决战，外加技能费用编辑优化，版本号BATL_v0.9.0_beta", bullet=True)
                # with dpg.group(horizontal=True, horizontal_spacing=0):
                #     dpg.add_text("2024.09.29  \t一堆bug修复和功能优化，版本号BATL_v0.9.1_beta    （特别鸣谢来BATL酒吧花式点炒饭的这个B 站用户：", bullet=True)
                #     dpg.add_button(label='@rkc018', small=True, callback=lambda:webbrowser.open('https://space.bilibili.com/7727552'))
                #     dpg.add_text("）")
                # dpg.add_text("2024.10.01-2024.10.07 \t国庆狠狠摸鱼", bullet=True, color=(128,128,128))
                # dpg.add_text("2024.10.08  \t现已支持中文路径，且恢复“打开文件夹”功能，版本号BATL_v0.9.2_beta", bullet=True)
                # dpg.add_text("2024.10.11 \tui界面优化，新增夜间模式主题，版本号BATL_v0.9.3_beta", bullet=True)
                # dpg.add_text("2024.10.17 \t新增学生头像相关功能，修改学生文件和关卡文件格式（旧版文件不再支持），版本号BATL_v0.10.0_beta", bullet=True)
                # dpg.add_text("2024.10.18 \t新增从作战记录导出学生功能，版本号BATL_v0.10.1_beta", bullet=True)
                # dpg.add_text("2024.10.23 \t新增费用轴自动计算功能，版本号BATL_v0.10.2_beta", bullet=True)
                # dpg.add_text("2024.10.25 \t新增撤销与重做功能，版本号BATL_v0.10.3_beta", bullet=True)
                # dpg.add_text("2024.10.28 \t优化作战计划中的事件显示，版本号BATL_v0.10.4_beta", bullet=True)
                # dpg.add_text("2024.10.29 \t新增支持添加其他单位（如奶奶灯、拘束弹控制器等），版本号BATL_v0.10.5_beta", bullet=True)
            dpg.add_spacer(height=20)
            # dpg.add_text("to do list")
            # dpg.bind_item_font(dpg.last_item(), cn_font_medium)
            # dpg.add_separator()
            with dpg.collapsing_header(label='to do list'):
                # dpg.bind_item_font(dpg.last_item(), cn_font_medium)
                dpg.add_text("【已完成】优化建议：学生名和保存文件名交换位置", bullet=True)
                dpg.add_text("【已完成】优化建议：资源管理器中改文件名后，下次读取时将改了的文件名放在“保存文件名”处，暂时不直接修改csv内数值，但下次保存时会自动覆盖", bullet=True)
                dpg.add_text("【已完成】优化建议：学生编辑页面，EX和NS输入框对齐", bullet=True)
                dpg.add_text("【已完成】优化建议：添加重复学生时弹窗报错", bullet=True)
                dpg.add_text("【已完成】优化建议：作战计划页面，支持多选学生", bullet=True)
                dpg.add_text("【已完成】优化建议：实操模拟 滚轮控制增减1秒", bullet=True)
                dpg.add_text('【已完成】优化建议：时间输入统一为“分:秒”格式（目前全都是以“秒”为单位，不接受“分”输入', bullet=True)
                dpg.add_text('【已完成】问题修复：由于pyinstaller的封装逻辑，“打开文件夹”功能损坏，暂时已隐藏，未来可能考虑修复', bullet=True)
                dpg.add_text("【已完成】问题修复：原生file_dialog不支持中文路径，需要添加替代方案", bullet=True)
                dpg.add_text("【已完成】新增功能：实操参考面板，备注栏改为可编辑，且关闭窗口时将填写的备注同步至作战计划", bullet=True)
                dpg.add_text("【已完成】新增功能：学生编辑页面，新增备注栏；同时内核的Student类增加类变量“备注”", bullet=True)
                dpg.add_text("【已完成】修改：选择文件返回为空时，添加handler", bullet=True)
                dpg.add_text("【已完成】新增功能：学生头像显示", bullet=True)
                dpg.add_text("【已完成】新增功能：从作业文件（作战计划文件）导出学生至student_files", bullet=True)
                dpg.add_text("【已完成】新增功能：费用轴自动计算（寻找水星、轮椅等关键字及其技能时间，自动添加回费速率节点）", bullet=True)
                dpg.add_text("【已完成】新增功能：作战计划页面新增撤销/重做功能，最多撤销15次：每次使用refresh_plan_table时，将当前mission.log存至栈中，并用另一个栈保存重做数据。refresh_battle_plan会清空栈", bullet=True)
                dpg.add_text("【已完成】修改：敌人事件也改为长条按钮显示", bullet=True)
                dpg.add_text("【已完成】新增功能：支持多个敌人，但敌人事件条和buff条还是一起显示", bullet=True)
                dpg.add_text("【已完成】修改：事件条按钮消去重叠部分，即按需缩短长条部分的长度；xx.8时的事件所在格有错，查错", bullet=True)
                # dpg.add_text("【摆了，偷偷注释掉】小bug修改：不显示其他单位受击和buff时，部分情况下第一个事件条/敌人buff条会有3像素左右的位移", bullet=True)


                dpg.add_text("暂时无解问题：初始化较慢，且期间不能拖动窗口", bullet=True)
                dpg.add_text("暂时无解问题：输入中文时存在卡顿", bullet=True)
                # dpg.add_spacer(height=20)
                # dpg.add_text('可能改进点（仅列出，待评定）：')
                # dpg.bind_item_font(dpg.last_item(), cn_font_medium)
                # dpg.add_separator()
                # dpg.add_text('作战时间轴性能优化：不是每次新增技能后都重新拉表，而是在原表基础上只修改部分格。代价是开发难度较大时间较长（这点和用户无关），出错可能性较高')
                # dpg.add_text('若上述优化完成，可以扩展拖动添加范围，用户可以直接把技能拖到“时间-目标”对应所在格，就不用手动选取目标了')
        
        with dpg.tab(label="debug"):
            def debug_terminal(sender, app_data):
                try:
                    code = dpg.get_value('debug_terminal')
                    code2 = "\ndpg.set_value('debug_output_variable', str(debug_output))"
                    exec(code+code2)
                except Exception as e:
                    print(f"ERROR: {e}")
            dpg.add_text('******   DO NOT DO ANYTHING IN THIS PAGE BEFORE YOU KNOW WHAT YOU ARE DOING!   ******')
            dpg.add_input_text(label='debug_terminal', tag='debug_terminal', width=800, height=250, default_value="debug_output = '\\n'.join([str(key)+'\\t'+str(value) for key,value in mission.log.items()])", multiline=True)
            with dpg.group(horizontal=True):
                dpg.add_button(label='code execute', width=150, height=30, callback=debug_terminal)
                dpg.add_button(label='default input', width=150, height=30, callback=lambda:dpg.set_value('debug_terminal', "debug_output = '\\n'.join([str(key)+'\\t'+str(value) for key,value in mission.log.items()])"))
                # 替换输出至debug_log 第2部分
                dpg.add_button(label='get terminal output', width=150, height=30, callback=lambda:dpg.set_value('debug_output_variable', output.getvalue()))
            dpg.add_input_text(label='debug_output', width=800, height=250, source='debug_output_variable', multiline=True, readonly=True)

    
            
with dpg.window(label='LOADING', tag='loading_window', width=1200, height=800, no_close=True):
    dpg.add_text('Loading......')
    dpg.add_text('Please wait for about 10 seconds......')
    dpg.add_text('DO NOT move this window(BATL.exe) until this message is disappeared (Otherwise may cause the program to freeze)')
    dpg.add_loading_indicator(style=1)
    dpg.add_image("dont_move_img_texture")




# dpg.bind_theme('main_theme')

# 启动应用
dpg.create_viewport(title=f'BA TimeLiner - v{BATL_VERSION} beta - powered by giga-35b', width=1200, height=800, small_icon='texture_files/others/Yuuka_calculator.ico')
dpg.set_viewport_pos((80, 40))
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("ba_timeliner", True)
# dpg.set_primary_window('loading_window', True)
# dpg.start_dearpygui()
frame_count = 0
last_column_0_width = dpg.get_item_state(column_0_width_container)["content_region_avail"][0]
last_column_1_width = dpg.get_item_state(column_1_width_container)["content_region_avail"][0]
last_column_2_width = dpg.get_item_state(column_2_width_container)["content_region_avail"][0]
last_column_3_width_list = [dpg.get_item_state(i)["content_region_avail"][0] for i in column_3_width_container_list]
last_vp_height = dpg.get_viewport_height()
student_file_saved_text_frame_count = 0
student_file_exported_text_frame_count = 0
mission_file_saved_text_frame_count = 0
copied_text_frame_count = 0

# 和DPG渲染帧数强挂钩的函数
while dpg.is_dearpygui_running():
    # 加载好之前显示loading_window
    if frame_count<30:
        pass
    else:
        dpg.hide_item("loading_window")

    # DPG渲染
    dpg.render_dearpygui_frame()

    # 学生文件和关卡文件保存显示文字的主动隐去
    if dpg.get_value('student_file_saved_text')!='':
        student_file_saved_text_frame_count += 1
    if student_file_saved_text_frame_count>=180:
        dpg.set_value('student_file_saved_text', '')
        student_file_saved_text_frame_count = 0
    if dpg.get_value('student_file_exported_text')!='':
        student_file_exported_text_frame_count += 1
    if student_file_exported_text_frame_count>=180:
        dpg.set_value('student_file_exported_text', '')
        student_file_exported_text_frame_count = 0
    if dpg.get_value('mission_file_saved_text')!='':
        mission_file_saved_text_frame_count += 1
    if mission_file_saved_text_frame_count>=180:
        dpg.set_value('mission_file_saved_text', '')
        mission_file_saved_text_frame_count = 0
    if dpg.does_item_exist('copied_text'):
        if dpg.get_value('copied_text')!='':
            copied_text_frame_count += 1
        if copied_text_frame_count>=180:
            dpg.set_value('copied_text', '')
            copied_text_frame_count = 0
    
    # 作战时间轴页面，buff条随列宽变动而改变位置
    if frame_count>=60 and not dpg.does_item_exist('temp_spacer') and dpg.does_item_exist(column_2_width_container):
        column_0_width = dpg.get_item_state(column_0_width_container)["content_region_avail"][0]
        column_1_width = dpg.get_item_state(column_1_width_container)["content_region_avail"][0]
        column_2_width = dpg.get_item_state(column_2_width_container)["content_region_avail"][0]
        column_3_width_list = [dpg.get_item_state(i)["content_region_avail"][0] for i in column_3_width_container_list]
        if column_0_width==last_column_0_width and column_1_width==last_column_1_width and column_2_width==last_column_2_width and column_3_width_list==last_column_3_width_list:
            pass
        else:
            last_column_0_width = column_0_width
            last_column_1_width = column_1_width
            last_column_2_width = column_2_width
            last_column_3_width_list = column_3_width_list.copy()
            def buff_bar_pos_x_cal(column, in_column_index):
                column_2_baseline = column_0_width + column_1_width + 13 + 9*2
                column_3_baseline = column_2_baseline + column_2_width + 56 + 9
                bar_width = 13    #内置1像素间隙
                if column==2:
                    pos_x = column_2_baseline + in_column_index*bar_width
                else:
                    pos_x = column_3_baseline + sum(column_3_width_list[:column-3]) + 9*(column-3) + in_column_index*bar_width

                return pos_x
            def event_bar_pos_x_cal(type, in_column_index):
                bar_width = 13    #内置1像素间隙
                column_2_baseline = column_0_width + column_1_width + 13 + 2*9 + 3*bar_width
                pos_x = column_2_baseline + in_column_index*bar_width

                return pos_x

            for item in dpg.get_item_children('in_table_buff_group', slot=1):
                if dpg.get_item_type(item)=='mvAppItemType::mvButton':
                    column, in_column_index, start_time = dpg.get_item_user_data(item)
                    original_pos = dpg.get_item_pos(item)
                    dpg.set_item_pos(item, (buff_bar_pos_x_cal(column, in_column_index),original_pos[1]))
            for item in dpg.get_item_children('in_table_event_group', slot=1):
                if dpg.get_item_type(item)=='mvAppItemType::mvButton':
                    event_type, in_column_index, start_time = dpg.get_item_user_data(item)
                    original_pos = dpg.get_item_pos(item)
                    dpg.set_item_pos(item, (event_bar_pos_x_cal(event_type, in_column_index),original_pos[1]))
            # print('pos_x_reset')

    # 作战时间轴页面，作战计划窗口高度随BATL窗口高度改变而改变
    if frame_count>=60:
        vp_height = dpg.get_viewport_height()
        if vp_height!=last_vp_height:
            last_vp_height = vp_height
            dpg.set_item_height('plan_table_window', max(540,vp_height-260))
            

    frame_count += 1
dpg.destroy_context()

# 替换输出至debug_log 第3部分
sys.stdout = sys.__stdout__
sys.stderr = sys.__stderr__
output.close()

