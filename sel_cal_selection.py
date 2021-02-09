# # full zoom out
# left_mnth_slector = "/html/body/div[2]/div/div/div/div/div[1]/div[1]/div[2]/div[1]/div/span/a[2]"
# driver.find_element_by_xpath(left_mnth_slector).click()
# left_year_slector = "/html/body/div[2]/div/div/div/div/div[1]/div[1]/div[2]/div[1]/div[2]/div/div[1]/a[2]"
# driver.find_element_by_xpath(left_year_slector).click()
# left_decade_slector = "/html/body/div[2]/div/div/div/div/div[1]/div[1]/div[2]/div[1]/div[2]/div/div[1]/a[2]"
# driver.find_element_by_xpath(left_decade_slector).click()
# time.sleep(3)

# start_date = datetime.datetime.strptime("2021-01-01", "%Y-%m-%d")
# end_date = datetime.datetime.strptime("2021-01-01", "%Y-%m-%d")

# decades = {
#     1: "2010-2019",
#     2: "2020-2029",
# }

# driver.find_element_by_link_text(decades[2]).click()
# time.sleep(3)

# year = 2021
# year_table_xpath = "/html/body/div[2]/div/div/div/div/div[1]/div[1]/div[2]/div[1]/div[2]/div/div[2]/table/tbody"
# # for loops over the year table
# clicked = False
# for i in range(1, 4):
#     for j in range(1, 5):
#         year_xpath = year_table_xpath + f"/tr[{i}]/td[{j}]/a"
#         elem_year = driver.find_element_by_xpath(year_xpath)
#         if elem_year.is_enabled() and elem_year.text == str(year):
#             elem_year.click()
#             clicked = True
#             break
#     if clicked:
#         break
# time.sleep(3)

# month = 1
# mnths_nums = np.arange(12).reshape(4, 3)
# # indexing in xpath starts from 1 not 0
# mnth_row = np.where(mnths_nums == month - 1)[0][0] + 1
# mnth_col = np.where(mnths_nums == month - 1)[1][0] + 1
# print(mnth_col, mnth_row)
# month_table_xpath = "/html/body/div[2]/div/div/div/div/div[1]/div[1]/div[2]/div[1]/div[2]/div/div[2]/table/tbody"
# driver.find_element_by_xpath(
#     month_table_xpath + f"/tr[{mnth_row}]/td[{mnth_col}]/a").click()
# time.sleep(3)

# date = 14
# date_table_xpath = "/html/body/div[2]/div/div/div/div/div[1]/div[2]/div[2]/div[2]/table/tbody"
# # for loops over the date table
# clicked = False
# for i in range(1, 7):
#     for j in range(1, 8):
#         date_xpath = date_table_xpath + f"/tr[{i}]/td[{j}]"
#         elem_date = driver.find_element_by_xpath(date_xpath)
#         if elem_date.is_enabled() and elem_date.text == str(date):
#             print(elem_date.get_attrubute("title"))
#             elem_date.click()
#             clicked = True
#             break
#     if clicked:
#         break
# time.sleep(3)

# # month_table_xpath = "/html/body/div[2]/div/div/div/div/div[1]/div[2]/div[2]/div[2]/table/tbody"
# # # for loops over the month table
# # for i in range(1, 4):
# #     for j in range(1, 5):
# #         month_xpath = date_table_xpath + f"/tr[{i}]/td[{j}]"
# #         elem_month = driver.find_element_by_xpath(date_xpath)
# #         if elem_month.is_enabled() and elem_month.text == str(month):
# #             print(elem_month.get_attrubute("title"))
# #             elem_month.click()
