class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class DanhSachLienKet:
  def __init__(self):
    self.head = None

  def chen_vao_cuoi(self, data):
    nut_moi = Node(data)
    if not self.head:
      self.head = nut_moi
      return

    hien_tai = self.head
    while hien_tai.next:
      hien_tai = hien_tai.next
    hien_tai.next = nut_moi

  def hien_thi(self):
    hien_tai = self.head
    while hien_tai:
      print(hien_tai.data, end=" ")
      hien_tai = hien_tai.next
    print()


danh_sach = DanhSachLienKet()
danh_sach.chen_vao_cuoi(5)
danh_sach.chen_vao_cuoi(10)
danh_sach.chen_vao_cuoi(15)
danh_sach.hien_thi()