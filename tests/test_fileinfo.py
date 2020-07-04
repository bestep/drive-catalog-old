import os

from drive_catalog import fileinfo


def test_image_type_jpg():
    path = os.path.join(os.getcwd(),
                        'testdrive/coffee_beans_coffee_drink.jpg')
    result = fileinfo.get_file_info(path)
    assert result[0]['type'] == 'Image'


def test_image_type_jpx():
    path = os.path.join(os.getcwd(), 'testdrive/lilac.jpx')
    result = fileinfo.get_file_info(path)
    assert result[0]['type'] == 'Image'


def test_image_type_png():
    path = os.path.join(os.getcwd(), 'testdrive/lilac.png')
    result = fileinfo.get_file_info(path)
    assert result[0]['type'] == 'Image'


def test_image_type_gif():
    path = os.path.join(os.getcwd(), 'testdrive/lilac.gif')
    result = fileinfo.get_file_info(path)
    assert result[0]['type'] == 'Image'


def test_image_type_jpeg():
    path = os.path.join(os.getcwd(), 'testdrive/lilac.jpeg')
    result = fileinfo.get_file_info(path)
    assert result[0]['type'] == 'Image'


def test_image_type_tif():
    path = os.path.join(os.getcwd(), 'testdrive/lilac.tif')
    result = fileinfo.get_file_info(path)
    assert result[0]['type'] == 'Image'


def test_image_type_bmp():
    path = os.path.join(os.getcwd(), 'testdrive/lilac.bmp')
    result = fileinfo.get_file_info(path)
    assert result[0]['type'] == 'Image'


def test_image_type_psd():
    path = os.path.join(os.getcwd(), 'testdrive/lilac.psd')
    result = fileinfo.get_file_info(path)
    assert result[0]['type'] == 'Image'


def test_image_type_heic():
    path = os.path.join(os.getcwd(), 'testdrive/lilac.heic')
    result = fileinfo.get_file_info(path)
    assert result[0]['type'] == 'Image'


def test_image_type_eps():
    path = os.path.join(os.getcwd(), 'testdrive/lilac.eps')
    result = fileinfo.get_file_info(path)
    assert result[0]['type'] == 'Image'


def test_image_type_svg():
    path = os.path.join(os.getcwd(), 'testdrive/lilac.svg')
    result = fileinfo.get_file_info(path)
    assert result[0]['type'] == 'Image'


def test_image_type_tiff():
    path = os.path.join(os.getcwd(), 'testdrive/lilac.tiff')
    result = fileinfo.get_file_info(path)
    assert result[0]['type'] == 'Image'


def test_image_type_webp():
    path = os.path.join(os.getcwd(), 'testdrive/lilac.webp')
    result = fileinfo.get_file_info(path)
    assert result[0]['type'] == 'Image'


def test_video_type_mov():
    path = os.path.join(os.getcwd(), 'testdrive/test.mov')
    result = fileinfo.get_file_info(path)
    assert result[0]['type'] == 'Video'


def test_video_type_mp4():
    path = os.path.join(os.getcwd(), 'testdrive/AboutBan1935.mp4')
    result = fileinfo.get_file_info(path)
    assert result[0]['type'] == 'Video'


def test_video_type_m4v():
    path = os.path.join(os.getcwd(), 'testdrive/test.m4v')
    result = fileinfo.get_file_info(path)
    assert result[0]['type'] == 'Video'


def test_video_type_mkv():
    path = os.path.join(os.getcwd(), 'testdrive/test.mkv')
    result = fileinfo.get_file_info(path)
    assert result[0]['type'] == 'Video'


def test_video_type_webm():
    path = os.path.join(os.getcwd(), 'testdrive/test.webm')
    result = fileinfo.get_file_info(path)
    assert result[0]['type'] == 'Video'


def test_video_type_mpeg():
    path = os.path.join(os.getcwd(), 'testdrive/test.mpeg')
    result = fileinfo.get_file_info(path)
    assert result[0]['type'] == 'Video'


def test_video_type_avi():
    path = os.path.join(os.getcwd(), 'testdrive/test.avi')
    result = fileinfo.get_file_info(path)
    assert result[0]['type'] == 'Video'


def test_video_type_wmv():
    path = os.path.join(os.getcwd(), 'testdrive/test.wmv')
    result = fileinfo.get_file_info(path)
    assert result[0]['type'] == 'Video'


def test_video_type_mpg():
    path = os.path.join(os.getcwd(), 'testdrive/test.mpg')
    result = fileinfo.get_file_info(path)
    assert result[0]['type'] == 'Video'


def test_video_type_flv():
    path = os.path.join(os.getcwd(), 'testdrive/test.flv')
    result = fileinfo.get_file_info(path)
    assert result[0]['type'] == 'Video'


def test_video_type_mts():
    path = os.path.join(os.getcwd(), 'testdrive/test.mts')
    result = fileinfo.get_file_info(path)
    assert result[0]['type'] == 'Video'


def test_video_type_ogv():
    path = os.path.join(os.getcwd(),
                        'testdrive/Early_1970s_Television_Commercials.ogv')
    result = fileinfo.get_file_info(path)
    assert result[0]['type'] == 'Video'


def test_video_type_mp3():
    path = os.path.join(os.getcwd(), 'testdrive/Groucho_01.mp3')
    result = fileinfo.get_file_info(path)
    assert result[0]['type'] == 'Audio'


def test_video_type_m4a():
    path = os.path.join(os.getcwd(), 'testdrive/Groucho_01.m4a')
    result = fileinfo.get_file_info(path)
    assert result[0]['type'] == 'Audio'


def test_video_type_ogg():
    path = os.path.join(os.getcwd(), 'testdrive/Groucho_01.ogg')
    result = fileinfo.get_file_info(path)
    assert result[0]['type'] == 'Audio'


def test_video_type_flac():
    path = os.path.join(os.getcwd(), 'testdrive/Groucho_01.flac')
    result = fileinfo.get_file_info(path)
    assert result[0]['type'] == 'Audio'


def test_video_type_wav():
    path = os.path.join(os.getcwd(), 'testdrive/Groucho_01.wav')
    result = fileinfo.get_file_info(path)
    assert result[0]['type'] == 'Audio'


def test_video_type_aac():
    path = os.path.join(os.getcwd(), 'testdrive/Groucho_01.aac')
    result = fileinfo.get_file_info(path)
    assert result[0]['type'] == 'Audio'


def test_video_type_mid():
    path = os.path.join(os.getcwd(), 'testdrive/test.mid')
    result = fileinfo.get_file_info(path)
    assert result[0]['type'] == 'Audio'


def test_video_type_midi():
    path = os.path.join(os.getcwd(), 'testdrive/test.midi')
    result = fileinfo.get_file_info(path)
    assert result[0]['type'] == 'Audio'


def test_video_type_oga():
    path = os.path.join(os.getcwd(), 'testdrive/test.oga')
    result = fileinfo.get_file_info(path)
    assert result[0]['type'] == 'Audio'


def test_video_type_opus():
    path = os.path.join(os.getcwd(), 'testdrive/Groucho_01.opus')
    result = fileinfo.get_file_info(path)
    assert result[0]['type'] == 'Audio'


def test_video_type_weba():
    path = os.path.join(os.getcwd(), 'testdrive/test.weba')
    result = fileinfo.get_file_info(path)
    assert result[0]['type'] == 'Audio'
