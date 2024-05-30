class Student:
    count = 0

    def __init__(self, id, name, total_score):
        self.id = id
        self.name = name
        self.total_score = total_score
        Student.count += 1

    def get_id(self):
        return self.id

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def get_total_score(self):
        return self.total_score

    def set_total_score(self, total_score):
        self.total_score = total_score

    def show_info(self):
        print(f"\nThông tin Sinh Viên:\n")
        print(f"MSV: {self.get_id()}")
        print(f"Tên Sinh Viên: {self.get_name()}")
        print(f"Điểm Tổng: {self.get_total_score()}")

ds = []

def input_integer(prompt):
    while True:
        value = input(prompt)
        if all(char.isdigit() for char in value):
            return int(value)
        else:
            print("Lỗi: Bạn phải nhập số. Vui lòng nhập lại!")


def input_float(prompt):
    while True:
        value = input(prompt)
        if all(char.isdigit() or char == '.' for char in value):
            return float(value)
        else:
            print("Lỗi: Bạn phải nhập số thực. Vui lòng nhập lại!")

def save_to_file(filename):
    with open(filename, 'w') as file:
        for student in ds:
            file.write(f"{student.get_id()},{student.get_name()},{student.get_total_score()}\n")
    print("Dữ liệu đã được lưu vào file ", filename)

def load_from_file(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                id, name, total_score = line.strip().split(',')
                sv = Student(int(id), name, float(total_score))
                ds.append(sv)
        print("Dữ liệu đã được tải từ file ", filename)
    except FileNotFoundError:
        print("Không tìm thấy file ", filename)

def main():
    load_from_file("thong_tin")

    while True:
        print(f'''\n
        0. Thoát Chương trình
        1. Thêm Sinh Viên
        2. Cập nhật thông tin sinh viên
        3. Xóa sinh viên
        4. Xem thông tin tất cả sinh viên
        5. Tìm sinh viên theo MSV
        6. Tìm sinh viên theo Tên
        7. Số lượng Sinh viên
        8. Tìm sinh viên theo Điểm Tổng
        ''')
        select = input_integer("Mời chọn chức năng:  ")

        if select == 0:
            break
        elif select == 1:
            id = input_integer("Nhập MSV: ")
            name = input("Nhập tên sinh viên: ")
            total_score = input_float("Nhập điểm tổng: ")
            sv = Student(id, name, total_score)
            ds.append(sv)
            print("Thêm sinh viên thành công!")

        elif select == 2:
            id = input("Nhập MSV của sinh viên cần sửa: ")
            found = False
            for i in ds:
                if i.get_id() == id:
                    i.set_name(input("Nhập vào tên mới: "))
                    i.set_total_score(input_float("Nhập vào điểm tổng mới: "))
                    i.show_info()
                    found = True
                    print("Cập nhật thông tin sinh viên thành công!")
                    break
            if not found:
                print("Không tìm thấy sinh viên với Id:", id)

        elif select == 3:
            id = input_integer("Nhập Id Sinh viên cần xóa: ")
            found = False
            for i in ds:
                if i.get_id() == id:
                    ds.remove(i)
                    found = True
                    print("Bạn đã xóa sinh viên thành công!")
                    break
            if not found:
                print("Không tìm thấy sinh viên với Id:", id)

        elif select == 4:
            if not ds:
                print("\nHiện không có sinh viên nào trong danh sách. Bạn vui lòng thêm sinh viên mới vào danh sách!")
            else:
                print(f"\nHiện có {len(ds)} sinh viên")
                for i in ds:
                    i.show_info()

        elif select == 5:
            id = input_integer("Nhập MSV: ")
            found = False
            for i in ds:
                if i.get_id() == id:
                    i.show_info()
                    found = True
                    break
            if not found:
                print("Không tìm thấy sinh viên với mã MSV:", id)

        elif select == 6:
            ten = input("Nhập tên sinh viên: ")
            found = False
            for i in ds:
                if i.get_name().lower() == ten.lower():
                    i.show_info()
                    found = True
            if not found:
                print("Không tìm thấy sinh viên với tên:", ten)

        elif select == 7:
            print(f"\nHiện có {len(ds)} sinh viên\n")

        elif select == 8:
            total_score = input_float("Nhập điểm tổng : ")
            found = False
            for i in ds:
                if i.get_total_score() == total_score:
                    i.show_info()
                    found = True
            if not found:
                print("Không tìm thấy sinh viên với điểm tổng:", total_score)

        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn lại!")

    save_to_file("thong_tin")

if __name__ == "__main__":
    main()
