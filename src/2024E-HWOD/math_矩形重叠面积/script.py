"""
【矩形相交的面积】在坐标系中，给定3组坐标(x, y, w, h)，-1000<=x,y<1000，w，h为正整数。
(x, y, w, h) 表示平面直角坐标系中的一个矩形：
x,y 为矩形左上角坐标点，w:向右，h:向下。即：(x, y, w, h)表示(x, x+w)和(y, y-h)围成的矩形
区域。给定3个矩形，求相交区域的面积。
输入描述:
3行输入分别为3个矩形的位置，分别代表“左上角x坐标”，“左上角y坐标”，“w矩形宽”，“h矩形高”
输出描述:
输出3个矩形相交的面积，不相交的输出0
示例:
输入
1 6 4 4
3 5 3 4
0 3 7 3
输出
2
"""
def get_intersection_area(x1, y1, w1, h1, x2, y2, w2, h2):
    """
    计算两个矩形的相交区域面积
    """
    # 计算相交区域的左上角和右下角坐标
    intersect_x1 = max(x1, x2)  # 相交区域左上角x
    intersect_y1 = min(y1, y2)  # 相交区域左上角y
    intersect_x2 = min(x1 + w1, x2 + w2)  # 相交区域右下角x
    intersect_y2 = max(y1 - h1, y2 - h2)  # 相交区域右下角y

    # 相交区域的宽度和高度
    width = max(0, intersect_x2 - intersect_x1)
    height = max(0, intersect_y1 - intersect_y2)

    # 返回相交区域的面积
    return width * height

def main():
    # 读取输入：3个矩形的坐标与宽高
    #  x1, y1, w1, h1 = map(int, input().split())
    #  x2, y2, w2, h2 = map(int, input().split())
    #  x3, y3, w3, h3 = map(int, input().split())
    x1, y1, w1, h1 = 1, 6, 4, 4
    x2, y2, w2, h2 = 3, 5, 3, 4
    x3, y3, w3, h3 = 0, 3, 7, 3

    # 计算前两个矩形的相交区域面积
    area12 = get_intersection_area(x1, y1, w1, h1, x2, y2, w2, h2)

    # 计算两个矩形的相交区域和第三个矩形的相交面积
    if area12 > 0:
        # 获取前两个矩形相交区域与第三个矩形的相交面积
        intersection_x1 = max(x1, x2)
        intersection_y1 = min(y1, y2)
        intersection_w = min(x1 + w1, x2 + w2) - intersection_x1
        intersection_h = intersection_y1 - max(y1 - h1, y2 - h2)

        # 传递相交区域与第三个矩形计算交集
        final_area = get_intersection_area(intersection_x1, intersection_y1, intersection_w, intersection_h, x3, y3, w3, h3)
    else:
        final_area = 0

    # 输出最终相交面积
    print(final_area)

if __name__ == "__main__":
    main()

#  def intersection_area(x1, y1, w1, h1, x2, y2, w2, h2):
#      """计算两个矩形的相交面积"""
#      # 矩形1的边界
#      x1_right = x1 + w1
#      y1_bottom = y1 - h1
#
#      # 矩形2的边界
#      x2_right = x2 + w2
#      y2_bottom = y2 - h2
#
#      # 相交矩形的边界
#      intersect_left = max(x1, x2)
#      intersect_right = min(x1_right, x2_right)
#      intersect_top = min(y1, y2)
#      intersect_bottom = max(y1_bottom, y2_bottom)
#
#      # 计算交集宽和高
#      intersect_width = intersect_right - intersect_left
#      intersect_height = intersect_top - intersect_bottom
#
#      # 如果宽度和高度均大于0，说明有相交区域
#      if intersect_width > 0 and intersect_height > 0:
#          return intersect_width * intersect_height
#      return 0
#
#  # 输入读取
#  rect1 = list(map(int, input().split()))
#  rect2 = list(map(int, input().split()))
#  rect3 = list(map(int, input().split()))
#
#  # 计算前两个矩形的交集面积
#  area12 = intersection_area(*rect1, *rect2)
#
#  # 计算前两个矩形交集与第三个矩形的交集面积
#  if area12 > 0:
#      intersect_area = intersection_area(
#          max(rect1[0], rect2[0]),  # x1
#          min(rect1[1], rect2[1]),  # y1
#          min(rect1[0] + rect1[2], rect2[0] + rect2[2]) - max(rect1[0], rect2[0]),  # w
#          min(rect1[1], rect2[1]) - max(rect1[1] - rect1[3], rect2[1] - rect2[3]),  # h
#          *rect3
#      )
#      print(intersect_area)
#  else:
#      print(0)

