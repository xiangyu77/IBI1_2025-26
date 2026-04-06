# 肌酐清除率计算器
# 1. 获取用户输入的年龄、体重、性别、血肌酐浓度
# 2. 检查输入是否在合理范围内：
#     年龄 < 100
#     体重 > 20 且 < 80
#     肌酐 > 0 且 < 100
#     性别为 male 或 female
# 3. 如果有任何一项不满足，指出哪个变量需要修正，不计算CrCl
# 4. 如果所有输入有效，根据公式计算CrCl
#    CrCl = ((140 - 年龄) * 体重) / (72 * 肌酐)
#    如果是女性，再乘以0.85
# 5. 输出计算结果# 获取输入（注意input返回的是字符串，需要转换类型）
age = int(input("请输入年龄（岁）："))
weight = float(input("请输入体重（kg）："))
gender = input("请输入性别（male/female）：").strip().lower()
creatinine = float(input("请输入血肌酐浓度（umol/l）："))

# 输入验证
valid = True
error_msg = ""

if age >= 100:
    valid = False
    error_msg += "年龄必须小于100岁。\n"
if weight <= 20 or weight >= 80:
    valid = False
    error_msg += "体重必须在20kg到80kg之间。\n"
if creatinine <= 0 or creatinine >= 100:
    valid = False
    error_msg += "血肌酐浓度必须在0到100umol/l之间。\n"
if gender not in ["male", "female"]:
    valid = False
    error_msg += "性别必须是male或female。\n"

if not valid:
    print("输入错误：")
    print(error_msg)
else:
    # 计算CrCl
    CrCl = ((140 - age) * weight) / (72 * creatinine)
    if gender == "female":
        CrCl *= 0.85
    print("您的肌酐清除率为：", CrCl, "ml/min")