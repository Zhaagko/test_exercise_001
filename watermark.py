from PIL import Image
import requests

def get_binary_img (url: str) -> bytes:
    # загружаем изображение по ссылке
    img = requests.get(url, stream=True).raw
    return img

def add_watermark_to_img (img: bytes, watermark: bytes):
    # открываем изображения для редактирования
    image = Image.open(img)
    watermark = Image.open(watermark)

    #  создаем новое чистое изображение
    img_result = Image.new("RGBA", (watermark.size[0],
        (watermark.size[1] + image.size[1])))
    # обрезаем вотермарк
    watermark = watermark.crop((0, 0, 800, 132))
    # изменяем размер вотермарк
    watermark = watermark.resize((image.size[0], 132))
    # вставляем вотермарк на холст
    img_result.paste(watermark, (0, 0))
    # вставляем изображение товара на холст
    img_result.paste(image, (0, 132))

    return img_result

def save_png_image (image, file_name="base_filename") -> None:
    # сохраняем изображение в png-формате
    image.save(f"{file_name}.png")

if __name__  == "__main__":
    watermark_url = "http://alitair.1gb.ru/test_prog_plashki/benefit.png"
    image_url = "http://alitair.1gb.ru/test_prog_plashki/106044_benefit.jpg"

    img_bin = get_binary_img(image_url)
    watermark_bin = get_binary_img(watermark_url)

    image_with_watermark = add_watermark_to_img(img_bin, watermark_bin)

    save_png_image(image_with_watermark, "image_with_watermark")
