from LexicalScanner import scan

def main():
    file_path = input("Nhập đường dẫn tệp chương trình Visual C: ")

    words = scan(file_path)
    ofile_path = file_path[:-3] + ".vctok"
    with open(ofile_path, 'w') as output_file:
        for word in words:
            output_file.write(f"{word}\n")
        output_file.write("$")
    print(f"Kết quả đã được ghi vào tệp {ofile_path}")

if __name__ == "__main__":
    main()