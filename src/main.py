from LexicalAnalysis import LexicalAnalysis

def main():
    file_path = input("Nhập đường dẫn tệp chương trình Visual C: ")

    # words = scan(file_path)
    with open(file_path, 'r') as file:
        content = file.read()

    scanner = LexicalAnalysis()
    words = scanner.scan(content)
    vctokfile_path = file_path[:-3] + ".vctok"
    datfile_path = file_path[:-3] + ".dat"
    with open(vctokfile_path, 'w') as output_file:
        for word in words:
            output_file.write(f"{word}\n")
        output_file.write("$")
    print(f"Kết quả đã được ghi vào tệp {vctokfile_path}")
    scanner.export(datfile_path)

if __name__ == "__main__":
    main()