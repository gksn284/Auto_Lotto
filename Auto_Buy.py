import telegram
from selenium import webdriver
from selenium.webdriver.support.select import Select

def Buy():
    ID = '아이디 입력' # 개인정보
    PW = '비밀번호 입력'

    # 로또 로그인 접속
    driver = webdriver.Chrome('./chromedriver')
    driver.get('https://dhlottery.co.kr/user.do?method=login&returnUrl=')

    # 아이디 비밀번호 입력
    login_ID = driver.find_element_by_name('userId')
    login_ID.clear()
    login_ID.send_keys(ID)

    login_PW = driver.find_element_by_name('password')
    login_PW.clear()
    login_PW.send_keys(PW)

    # 로그인 클릭
    Login_Xpath = '//*[@id="article"]/div[2]/div/form/div/div[1]/fieldset/div[1]/a'
    driver.find_element_by_xpath(Login_Xpath).click()

    # 구매창 이동
    driver.get('https://el.dhlottery.co.kr/game/TotalGame.jsp?LottoId=LO40')

    # 자동 선택
    driver.switch_to.frame('ifrm_tab') # 프레임 안에 있음
    driver.find_element_by_xpath('//*[@id="num2"]').click()

    # 장수 선택
    Num = '2'
    ticket = Select(driver.find_element_by_xpath('//*[@id="amoundApply"]'))
    ticket.select_by_value(Num)

    # 확인 버튼 클릭
    driver.find_element_by_xpath('//*[@id="btnSelectNum"]').click()

    # 구매 버튼 클릭
    driver.find_element_by_xpath('//*[@id="btnBuy"]').click()

    # 확인 버튼
    alert = driver.switch_to.alert
    alert.accept()

    #|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

    try:
        Bot(driver.switch_to_alert().text)
        driver.quit
    except:
        # 번호 확인 창 이동
        driver.get('https://dhlottery.co.kr/myPage.do?method=lottoBuyListView')

        # 1주일, 조회 버튼 클릭
        driver.find_element_by_xpath('//*[@id="frm"]/table/tbody/tr[3]/td/span[2]/a[2]').click()
        driver.find_element_by_xpath('//*[@id="submit_btn"]').click()

        # 로또 용지 띄움
        driver.switch_to.frame('lottoBuyList')
        driver.find_element_by_xpath('/html/body/table/tbody/tr/td[4]/a').click()

        driver.close() # 메인 창은 닫고 로또 용지 창을 컨트롤
        driver.switch_to.window(driver.window_handles[-1])

        series = (driver.find_element_by_xpath('//*[@id="popup645paper"]/div[1]/h3/strong')).text # 회차
        issue = (driver.find_element_by_xpath('//*[@id="popup645paper"]/div[1]/ul/li[1]')).text # 발행일
        draw = (driver.find_element_by_xpath('//*[@id="popup645paper"]/div[1]/ul/li[2]')).text # 추첨일

        # A 자동 번호
        A_1 = (driver.find_element_by_xpath('//*[@id="popup645paper"]/div[2]/ul/li[1]/div/span['+str(1)+']')).text
        A_2 = (driver.find_element_by_xpath('//*[@id="popup645paper"]/div[2]/ul/li[1]/div/span['+str(2)+']')).text
        A_3 = (driver.find_element_by_xpath('//*[@id="popup645paper"]/div[2]/ul/li[1]/div/span['+str(3)+']')).text
        A_4 = (driver.find_element_by_xpath('//*[@id="popup645paper"]/div[2]/ul/li[1]/div/span['+str(4)+']')).text
        A_5 = (driver.find_element_by_xpath('//*[@id="popup645paper"]/div[2]/ul/li[1]/div/span['+str(5)+']')).text
        A_6 = (driver.find_element_by_xpath('//*[@id="popup645paper"]/div[2]/ul/li[1]/div/span['+str(6)+']')).text

        A_sum = "A 자동 :『" + A_1 + " " + A_2 + " " + A_3 + " " + A_4 + " " + A_5 + " " + A_6 + "』"

        # B 자동 번호
        B_1 = (driver.find_element_by_xpath('//*[@id="popup645paper"]/div[2]/ul/li[2]/div/span['+str(1)+']')).text
        B_2 = (driver.find_element_by_xpath('//*[@id="popup645paper"]/div[2]/ul/li[2]/div/span['+str(2)+']')).text
        B_3 = (driver.find_element_by_xpath('//*[@id="popup645paper"]/div[2]/ul/li[2]/div/span['+str(3)+']')).text
        B_4 = (driver.find_element_by_xpath('//*[@id="popup645paper"]/div[2]/ul/li[2]/div/span['+str(4)+']')).text
        B_5 = (driver.find_element_by_xpath('//*[@id="popup645paper"]/div[2]/ul/li[2]/div/span['+str(5)+']')).text
        B_6 = (driver.find_element_by_xpath('//*[@id="popup645paper"]/div[2]/ul/li[2]/div/span['+str(6)+']')).text

        B_sum = "B 자동 :『" + B_1 + " " + B_2 + " " + B_3 + " " + B_4 + " " + B_5 + " " + B_6 + "』"

        Sum = series + "\n" + issue + "\n" + draw + "\n" + A_sum + "\n" + B_sum
        Bot(Sum)

        driver.quit()


def Bot(x):                                    #봇을 통해 보낼 메세지를 x에 입력
    tok = "1534787741:AAHmXtFYOLHC6ybK3jevVT6WkoQq4v-Wsm4"
    bot = telegram.Bot(token = tok)

    bot.send_message(1467011786, x)
    return 0

Buy()
