from LexicalScanner import scan

def main():
    file_path = input("Nhập đường dẫn tệp chương trình Visual C: ")

    tokens = scan(file_path)
    ofile_path = file_path[:-3] + ".vctok"
    with open(ofile_path, 'w') as output_file:
        for token in tokens:
            output_file.write(f"{token}\n")
    print(f"Kết quả đã được ghi vào tệp {ofile_path}")

if __name__ == "__main__":
    main()