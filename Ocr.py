import ddddocr


def GetCodeFromByte(img_bytes):
    ocr = ddddocr.DdddOcr()
    res = ocr.classification(img_bytes)
    return res


def GetCodeFromFile(ImgName):
    ocr = ddddocr.DdddOcr()
    with open(ImgName, "rb") as f:
        img_bytes = f.read()
        res = ocr.classification(img_bytes)
    return res


if __name__ == "__main__":
    print(GetCodeFromFile("yzm.png"))
