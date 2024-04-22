class NhanVien:
    def __init__(self, maNV, tenNV, sdtNV, emailNV, vitriNV):
        self.maNV = maNV
        self.tenNV = tenNV
        self.sdtNV = sdtNV
        self.emailNV = emailNV
        self.vitriNV = vitriNV

    def get_maNV(self):
        return self.maNV
    def set_maNV(self, maNV):
        self.maNV = maNV

    def get_tenNV(self):
        return self.tenNV
    def set_tenNV(self, tenNV):
        self.tenNV = tenNV

    def get_sdtNV(self):
        return self.sdtNV
    def set_sdtNV(self, sdtNV):
        self.sdtNV = sdtNV

    def get_emailNV(self):
        return self.emailNV
    def set_emailNV(self, emailNV):
        self.emailNV = emailNV

    def get_vitriNV(self):
        return self.vitriNV
    def set_vitriNV(self, vitriNV):
        self.vitriNV = vitriNV

class QuanLy(NhanVien):
    def __init__(self, maNV, tenNV, sdtNV, emailNV, nhomQL, soNV_trong_nhomQL, tongDoanhThu):
        super().__init__(maNV, tenNV, sdtNV, emailNV, "Quản Lý")
        self.nhomQL = nhomQL
        self.soNV_trong_nhomQL = soNV_trong_nhomQL
        self.tongDoanhThu = tongDoanhThu

    def get_nhomQL(self):
        return self.nhomQL
    def set_nhomQL(self, nhomQL):
        self.nhomQL = nhomQL

    def get_soNV_trong_nhomQL(self):
        return self.soNV_trong_nhomQL
    def set_soNV_trong_nhomQL(self, soNV_trong_nhomQL):
        self.soNV_trong_nhomQL = soNV_trong_nhomQL

    def get_tongDoanhThu(self):
        return self.tongDoanhThu
    def set_tongDoanhThu(self, tongDoanhThu):
        self.tongDoanhThu = tongDoanhThu

class BanHang(NhanVien):
    def __init__(self, maNV, tenNV, sdtNV, emailNV, doanhThu, soThang_lamViec):
        super().__init__(maNV, tenNV, sdtNV, emailNV, "Bán Hàng")
        self.doanhThu = doanhThu
        self.soThang_lamViec = soThang_lamViec

    def get_doanhThu(self):
        return self.doanhThu
    def set_doanhThu(self, doanhThu):
        self.doanhThu = doanhThu

    def get_soThang_lamViec(self):
        return self.soThang_lamViec
    def set_soThang_lamViec(self, soThang_lamViec):
        self.soThang_lamViec = soThang_lamViec

class ManagerEmployee:
    def __init__(self):
        self.NV = []
        self.NV_saoLuu = []

    def add_NV(self, NhanVien):
        self.NV.append(NhanVien)
        print("Thêm nhân viên thành công!")

    def delete_NV(self, NhanVien,option):

        for nhanvien in self.NV:
            if nhanvien.maNV == NhanVien.maNV:
                if option == 1:
                    self.NV.remove(nhanvien)
                    print("Đã xóa vĩnh viễn nhân viên: {}".format(nhanvien.tenNV))
                elif option == 2:
                    self.NV.remove(nhanvien)
                    self.NV_saoLuu.append(nhanvien)
                    print("Đã xóa có bản sao lưu nhân viên: {}".format(nhanvien.tenNV))

    def search_NV(self, keyword):
        for nhanvien in self.NV:
            if keyword.lower() in nhanvien.tenNV.lower() or keyword.lower() == str(nhanvien.maNV).lower():
                print("Thông tin nhân viên được tìm thấy:")
                print("Mã nhân viên:", nhanvien.maNV)
                print("Tên nhân viên:", nhanvien.tenNV)
                print("Số điện thoại:", nhanvien.sdtNV)
                print("Email:", nhanvien.emailNV)
                print("Vị trí làm việc:", nhanvien.vitriNV)
                if nhanvien.vitriNV == "Quản Lý":
                    print("Nhóm quản lý:", nhanvien.nhomQL)
                    print("Số nhân viên trong nhóm quản lý:", nhanvien.soNV_trong_nhomQL)
                    print("Tổng doanh thu:", nhanvien.tongDoanhThu)
                elif nhanvien.vitriNV == "Bán Hàng":
                    print("Doanh thu:", nhanvien.doanhThu)
                    print("Số tháng làm việc:", nhanvien.soThang_lamViec)
                return
        print("Không tìm thấy nhân viên nào với từ khóa '{}'".format(keyword))

    def view_list_theoViTri(self, vitri):
        print("Danh sách nhân viên làm việc ở vị trí {}:".format(vitri.upper()))
        timThay = False
        for nhanvien in self.NV:
            if nhanvien.vitriNV == vitri:
                print("Mã nhân viên:", nhanvien.maNV)
                print("Tên nhân viên:", nhanvien.tenNV)
                print("Số điện thoại:", nhanvien.sdtNV)
                print("Email:", nhanvien.emailNV)
                print("Vị trí làm việc:", nhanvien.vitriNV)
                if vitri == "Quản Lý":
                    print("Nhóm quản lý:", nhanvien.nhomQL)
                    print("Số nhân viên trong nhóm quản lý:", nhanvien.soNV_trong_nhomQL)
                    print("Tổng doanh thu:", nhanvien.tongDoanhThu)
                elif vitri == "Bán Hàng":
                    print("Doanh thu:", nhanvien.doanhThu)
                    print("Số tháng làm việc:", nhanvien.soThang_lamViec)
                timThay = True
        if not timThay:
            print("hiện Không có nhân viên nào làm việc ở vị trí {}".format(vitri.upper()))

    def tinh_Luong(self,nhanvien):
        luong = 8000000
        if nhanvien.vitriNV == "Quản Lý":
            if nhanvien.soNV_trong_nhomQL > 0:
                luong += nhanvien.soNV_trong_nhomQL * 250000
            if nhanvien.tongDoanhThu > 0:
                luong += nhanvien.tongDoanhThu * 0.01
            return luong
    def nhanvienBanHang_lam_lau_nhat(self):
        soThangLamMax = 0
        ten = ""
        for nvBanHang in self.NV:
            if nvBanHang.vitriNV == "Bán Hàng" and nvBanHang.soThang_lamViec > soThangLamMax:
                soThangLamMax = nvBanHang.soThang_lamViec
                ten = nvBanHang.tenNV
        print("Nhân viên bán hàng có số tháng làm lâu nhất là: {} với {} tháng.".format(ten,soThangLamMax))
    def nhomQL_co_dong_NV_Nhat(self,top):
        count = 0
        soLuongNv = 0
        ten = ""
        for nvQuanLy in self.NV:
            if nvQuanLy.vitriNV == "Quản Lý" and nvQuanLy.soNV_trong_nhomQL > soLuongNv:
                count += 1
                soLuongNv = nvQuanLy.soNV_trong_nhomQL
                ten = nvQuanLy.tenNV
                print("TOP {}: với {} nhân viên do {} quản lý".format(count,soLuongNv,ten))
                if count == top:
                    return
if __name__ == '__main__':
    manager = ManagerEmployee()

    nv_moi = QuanLy(2020, "Đào Anh Đức", "019283823", "hahah@gmail.com", "Nhóm 4", 5, 5000)
    nv_moi_2 = BanHang(10229, "Đức Chiến", "01928377", "chien@gmail.com", 4000, 8)
    nv_moi_3 = QuanLy(20220, "Đào Anh nam", "3424324", "ssss@gmail.com", "Nhóm 7", 2, 4000)
    nv_moi_4 = QuanLy(323, "lâm Anh nam", "5424234234", "kkkkk@gmail.com", "Nhóm 8", 45, 300)
    manager.add_NV(nv_moi)
    manager.add_NV(nv_moi_2)
    manager.add_NV(nv_moi_3)
    manager.add_NV(nv_moi_4)
    manager.delete_NV(nv_moi,1)
    manager.search_NV("Đức Chiến")
    manager.search_NV("10229")
    manager.view_list_theoViTri("Bán Hàng")
    manager.view_list_theoViTri("Quản Lý")
    luong=manager.tinh_Luong(nv_moi_3)
    print(luong)
    manager.nhanvienBanHang_lam_lau_nhat()
    manager.nhomQL_co_dong_NV_Nhat(5)