while contador < 3:
      try:
          email = driver.find_element_by_name('to')
          email.send_keys(emails)
          sleep(1)
          #//*[@id=":8s"]
          #//*[@id=":8p"]
          #//*[@id=":pw"]
          #//*[@id=":69"]
          assunt = driver.find_element_by_name("subjectbox")
          assunt.send_keys(assunto)
          sleep(1)
          #//*[@id=":8x"]
          #//*[@id=":87"]
          #//*[@id=":pe"]
          #//*[@id=":8c"]
          msg = driver.find_element_by_css_selector("#\3a a3")
          msg.send_keys(mensagem)
          sleep(1)

          #//*[@id=":90"]
          #//*[@id=":qj"]
          #//*[@id=":9c"]
          #//*[@id=":9h"]
          enviar = driver.find_element_by_link_text('send')
          enviar.click()
          #//*[@id=":p4"]
          #//*[@id=":7x"]
          #//*[@id=":82"]
          #//*[@id=":82"]
          break
      except NoSuchElementException:
          email = driver.find_element_by_xpath('//*[@id=":pw"]')
          email.send_keys(emails)
          sleep(1)

          #//*[@id=":69"]
          assunt = driver.find_element_by_xpath('//*[@id=":pe"]')
          assunt.send_keys(assunto)
          sleep(1)

          #//*[@id=":8c"]
          msg = driver.find_element_by_xpath('//*[@id=":9c"]')
          msg.send_keys(mensagem)
          sleep(1)

          #//*[@id=":9h"]
          enviar = driver.find_element_by_xpath('//*[@id=":7x"]')
          enviar.click()
          #//*[@id=":82"]
      except NoSuchElementException:
          email = driver.find_element_by_xpath('//*[@id=":69"]')
          email.send_keys(emails)
          sleep(1)

          assunt = driver.find_element_by_xpath('//*[@id=":8c"]')
          assunt.send_keys(assunto)
          sleep(1)

          msg = driver.find_element_by_xpath('//*[@id=":9h"]')
          msg.send_keys(mensagem)
          sleep(1)

          enviar = driver.find_element_by_xpath('//*[@id=":82"]')
          enviar.click()

      except NoSuchElementException:
          email = driver.find_element_by_xpath('//*[@id=":8s"]')
          email.send_keys(emails)
          sleep(1)

          assunt = driver.find_element_by_xpath('//*[@id=":8x"]')
          assunt.send_keys(assunto)
          sleep(1)

          msg = driver.find_element_by_xpath('#//*[@id=":90"]')
          msg.send_keys(mensagem)
          sleep(1)

          enviar = driver.find_element_by_xpath('//*[@id=":82"]')
          enviar.click()

      contador = contador + 1


      # while contador < 3:
      #     try:
      #         buttom = driver.find_element_by_xpath('//*[@id=":36"]/div/div')
      #         buttom.click()
      #         break
      #     except NoSuchElementException:
      #         buttom = driver.find_element_by_xpath('//*[@id=":2x"]/div/div/text()')
      #         buttom.click()
      #     except NoSuchElementException:
      #         buttom = driver.find_element_by_xpath('//*[@id=":34"]/div/div')
      #         buttom.click()
      #     except NoSuchElementException:
      #         buttom = driver.find_element_by_xpath('//*[@id=":34"]/div/div/text()')
      #         buttom.click()
      #     except:
      #         buttom = driver.find_element_by_xpath('//*[@id=":2x"]/div/div)')
      #         buttom.click()
      #
      #     contador = contador + 1
      #//*[@id=":2x"]/div/div
      #//*[@id=":2x"]/div/div/text()
      #//*[@id=":34"]/div/div
      #//*[@id=":34"]/div/div/text()
      #//*[@id=":36"]/div/div
      #buttom = driver.find_element_by_xpath('//*[@id=":k4"]/div/div/div')
      #buttom.click()


      #se a mensagem de email foi enviado com sucesso aparecer
      #/html/body/div[7]/div[3]/div/div[1]/div[5]/div[1]/div/div[3]/div/div/div[2]
