from varasto import Varasto


def main():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)

    print(f"Mehuvarasto: {mehua}")
    print(f"Olutvarasto: {olutta}")

    print("olutta.ota_varastosta(1000.0), mehua.otaVarastosta(-32.9)")
    olutta.ota_varastosta(1000.0)
    mehua.ota_varastosta(-32.9)

    print(f"Olutvarasto: {olutta}")
    print(f"Mehuvarasto: {mehua}")


if __name__ == "__main__":
    main()
