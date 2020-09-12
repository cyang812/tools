# -*- coding: utf-8 -*-
# @Author: cyang
# @Date:   2020-09-12 08:45:32
# @Last Modified by:   cyang812
# @Last Modified time: 2020-09-12 10:50:52

#随机生成试卷，考察省会城市

import random,os

capitals = {
	'河北省': ['石家庄市', '唐山市', '保定市', '秦皇岛市'],
	'山西省': ['太原市', '大同市', '长治市', '临沂市'],
	'辽宁省': ['沈阳市', '大连市', '铁岭市' ,'抚顺市'],
	'吉林省': ['长春市', '吉林市', '松原市' ,'四平市'],
	'黑龙江省': ['哈尔滨市', '佳木斯市', '大庆市', '黑河市'],
	'江苏省': ['南京市', '苏州市', '扬州市', '无锡市'],
	'浙江省': ['杭州市', '台州市', '温州市', '宁波市'],
	'安徽省': ['合肥市', '安庆市', '黄山市', '芜湖市'],
	'福建省': ['福州市', '厦门市', '泉州市', '漳州市'],
	'江西省': ['南昌市', '上饶市', '九江市', '吉安市'],
	'山东省': ['济南市', '烟台市', '青岛市', '菏泽市'],
	'河南省': ['郑州市', '开封市', '洛阳市', '驻马店市'],
	'广东省': ['广州市', '深圳市', '东莞市', '惠州市'],
	'湖南省': ['长沙市', '株洲市', '湘潭市', '张家界市'],
	'湖北省': ['武汉市', '宜昌市', '黄石市', '荆门市'],
	'海南省': ['海口市', '三亚市', '儋州市', '琼海市'],
	'四川省': ['成都市', '南充市', '达州市', '乐山市'],
	'贵州省': ['贵阳市', '盘州市', '遵义市', '毕节市'],
	'云南省': ['昆明市', '玉溪市', '曲靖市', '保山市'],
	'陕西省': ['西安市', '宝鸡市', '延安市', '咸阳市'],
	'甘肃省': ['兰州市', '白银市', '酒泉市', '张掖市'],
	'青海省': ['西宁市', '海东市', '玉树市', '同仁市'],
	'台湾省': ['台北市', '新竹市', '桃园市', '高雄市'],
	'内蒙古自治区': ['呼和浩特市', '鄂尔多斯市', '呼伦贝尔市', '包头市'],
	'广西壮族自治区': ['南宁市', '桂林市', '柳州市', '北海市'],
	'西藏自治区': ['拉萨市', '日喀则市', '昌都市', '林芝市', '山南市'],
	'宁夏回族自治区': ['银川市', '石嘴山市', '吴忠市', '固原市', '中卫市'],
	'新疆维吾尔自治区': ['乌鲁木齐市', '克拉玛依市', '吐鲁番市','哈密市'],
}

for quizNum in range(35):
	quizFile = open('capitalsQuiz_%s.txt' % (quizNum + 1), 'w', encoding='utf-8')
	answerKeyFile = open('capitalsQuiz_answer_%s.txt' % (quizNum + 1), 'w', encoding='utf-8')

	quizFile.write('Name: \n Date:\n Period: \n')
	quizFile.write('-' * 20 + 'State Capitals Quiz (Form %s)' % (quizNum + 1) + '-' * 20)
	quizFile.write('\n')

	states = list(capitals.keys())
	random.shuffle(states)

	for questionNum in range(len(capitals)):
		# print(type(capitals[states[questionNum]][0]))
		correctAnswer = capitals[states[questionNum]][0]
		# print(type(capitals[states[questionNum]]))
		wrongAnswers = capitals[states[questionNum]][1:]
		# print(len(wrongAnswers))
		wrongAnswers = random.sample(wrongAnswers, 3)
		answerOptions = wrongAnswers + [correctAnswer]
		random.shuffle(answerOptions)

		quizFile.write('%s. 以下哪个城市是%s的省会？\n' % (questionNum + 1, states[questionNum]))
		for i in range(4):
			# print(answerOptions[i])
			quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))
		quizFile.write('\n')

		answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
	
	quizFile.close()
	answerKeyFile.close()

