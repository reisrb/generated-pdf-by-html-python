import pdfkit
from flask import Flask, send_file, render_template
from flask_cors import CORS
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

app = Flask(__name__)
CORS(app)



@app.route('/teste', methods=['GET'])
def testePdf():
  with open('templates/thymeleaf_template.html') as f:
    replaced = f.read().replace('[[${pdfData}]]', "{\"pdfUser\":{\"id\":1,\"nome\":\"Administrador\",\"email\":\"admin@admin.com\",\"senha\":null,\"tipo\":{\"id\":\"LOCAL\",\"nome\":\"Local\"},\"ativo\":true,\"telefoneCelular\":null},\"pdfPagamento\":\"Pagamento 1\",\"pdfInformacoesAdicionais\":\"dsajlkd jaslkjd aslkjd\",\"pdfConsumidorasTexto\":\"m - (CNPJ: 38.210.938/9102-83)/ f - (CNPJ: 38.210.938/9102-81)/ u - (CNPJ: 81.290.389/2108-39)\",\"pdfRazaoSocial\":\"  m, f, u\",\"pdfActualDate\":\"21 de junho de 2021\",\"pdfConsumidoras\":[{\"empresa\":{\"id\":1,\"apelido\":\"m\",\"nomeFantasia\":\"m\",\"cnpj\":\"38210938910283\",\"inscricaoEstadual\":\"\",\"isentoInscricaoEstadual\":false,\"razaoSocial\":\"m\",\"setor\":null,\"endereco\":{\"cep\":\"\",\"logradouro\":null,\"numero\":null,\"complemento\":null,\"bairro\":null,\"cidade\":null,\"estado\":null},\"contatos\":[{\"id\":1,\"tipo\":{\"id\":\"COMERCIAL\",\"nome\":\"Comercial\"},\"nome\":\"jp\",\"email\":\"exjoao@hotmail.com\",\"telefone\":{\"fixo\":null,\"celular\":\"39802138902\"},\"cargo\":\"\",\"cpf\":\"83092183018\",\"estadoCivil\":null,\"documento\":{\"tipo\":null,\"numero\":null},\"comprador\":true}],\"arquivos\":null,\"matriz\":true,\"status\":{\"id\":\"PENDENTE\",\"nome\":\"Pendente\"}},\"id\":1,\"geradorProprio\":false,\"unidade\":\"m\",\"distribuidora\":\"9\",\"instalacao\":\"9\",\"cnpj\":\"38210938910283\",\"volume\":9,\"tarifa\":{\"id\":\"VERDE\",\"nome\":\"Verde\"},\"unica\":1,\"ponta\":null,\"foraPonta\":null,\"subgrupo\":{\"id\":1,\"nome\":\"Subgrupo 1\"},\"razaoSocial\":\"m\",\"apelido\":\"m\",\"endereco\":{\"cep\":\"\",\"logradouro\":null,\"numero\":null,\"complemento\":null,\"bairro\":null,\"cidade\":null,\"estado\":null}},{\"empresa\":{\"id\":2,\"apelido\":\"f\",\"nomeFantasia\":\"f\",\"cnpj\":\"38210938910281\",\"inscricaoEstadual\":\"\",\"isentoInscricaoEstadual\":false,\"razaoSocial\":\"f\",\"setor\":null,\"endereco\":{\"cep\":\"\",\"logradouro\":null,\"numero\":null,\"complemento\":null,\"bairro\":null,\"cidade\":null,\"estado\":null},\"contatos\":[{\"id\":2,\"tipo\":{\"id\":\"COMERCIAL\",\"nome\":\"Comercial\"},\"nome\":\"jp\",\"email\":\"exjoao@hotmail.com\",\"telefone\":{\"fixo\":null,\"celular\":\"39802138902\"},\"cargo\":\"\",\"cpf\":\"83092183018\",\"estadoCivil\":null,\"documento\":{\"tipo\":null,\"numero\":null},\"comprador\":true}],\"arquivos\":null,\"matriz\":false,\"status\":{\"id\":\"PENDENTE\",\"nome\":\"Pendente\"}},\"id\":2,\"geradorProprio\":false,\"unidade\":\"f\",\"distribuidora\":\"9\",\"instalacao\":\"9\",\"cnpj\":\"38210938910281\",\"volume\":9,\"tarifa\":{\"id\":\"VERDE\",\"nome\":\"Verde\"},\"unica\":9,\"ponta\":null,\"foraPonta\":null,\"subgrupo\":{\"id\":1,\"nome\":\"Subgrupo 1\"},\"razaoSocial\":\"f\",\"apelido\":\"f\",\"endereco\":{\"cep\":\"\",\"logradouro\":null,\"numero\":null,\"complemento\":null,\"bairro\":null,\"cidade\":null,\"estado\":null}},{\"empresa\":{\"id\":3,\"apelido\":\"u\",\"nomeFantasia\":\"u\",\"cnpj\":\"81290389210839\",\"inscricaoEstadual\":\"\",\"isentoInscricaoEstadual\":false,\"razaoSocial\":\"u\",\"setor\":null,\"endereco\":{\"cep\":\"\",\"logradouro\":null,\"numero\":null,\"complemento\":null,\"bairro\":null,\"cidade\":null,\"estado\":null},\"contatos\":[{\"id\":3,\"tipo\":{\"id\":\"COMERCIAL\",\"nome\":\"Comercial\"},\"nome\":\"jp\",\"email\":\"exjoao@hotmail.com\",\"telefone\":{\"fixo\":null,\"celular\":\"39802138902\"},\"cargo\":\"\",\"cpf\":\"83092183018\",\"estadoCivil\":null,\"documento\":{\"tipo\":null,\"numero\":null},\"comprador\":true}],\"arquivos\":null,\"matriz\":false,\"status\":{\"id\":\"PENDENTE\",\"nome\":\"Pendente\"}},\"id\":3,\"geradorProprio\":false,\"unidade\":\"u\",\"distribuidora\":\"9\",\"instalacao\":\"9\",\"cnpj\":\"81290389210839\",\"volume\":9,\"tarifa\":{\"id\":\"VERDE\",\"nome\":\"Verde\"},\"unica\":9,\"ponta\":null,\"foraPonta\":null,\"subgrupo\":{\"id\":1,\"nome\":\"Subgrupo 1\"},\"razaoSocial\":\"u\",\"apelido\":\"u\",\"endereco\":{\"cep\":\"\",\"logradouro\":null,\"numero\":null,\"complemento\":null,\"bairro\":null,\"cidade\":null,\"estado\":null}}],\"pdfCondicoes\":[{\"id\":1,\"garantia\":{\"id\":\"DEPOSITO_CAUCAO\",\"nome\":\"Depósito Caução\"},\"mesesFaturamento\":15}],\"pdfGarantias\":\"Depósito Caução (15 meses)\",\"pdfProdutos\":[{\"id\":1,\"dataInicio\":\"08/07/2021\",\"dataFim\":\"09/07/2021\",\"tipo\":{\"id\":\"UNICO\",\"nome\":\"Único\"},\"ofertas\":[{\"id\":1,\"dataInicio\":\"08/07/2021\",\"dataFim\":\"09/07/2021\",\"submercado\":{\"id\":\"SE_CO\",\"nome\":\"SE/CO\"},\"volume\":1,\"valor\":1,\"percentualAtendimentoCarga\":\"1\",\"percentualDescontoPreco\":\"\"}],\"preco\":{\"tipo\":{\"id\":\"COM_REAJUSTE\",\"nome\":\"Com Reajuste\"},\"indice\":{\"id\":\"IPCA\",\"nome\":\"IPCA\"},\"percentual\":\"100%\",\"dataBase\":\"10/2020\",\"dataBaseReajuste\":\"10/2021\"},\"flex\":{\"tipo\":{\"id\":\"COM_LIMITADORES\",\"nome\":\"Com Limitadores\"},\"minimo\":\"-1\",\"maximo\":\"1\",\"spread\":0},\"modulacao\":{\"tipo\":{\"id\":\"COM_LIMITADORES\",\"nome\":\"Com Limitadores\"},\"minimo\":\"-2\",\"maximo\":\"2\"},\"sazonalizacao\":{\"tipo\":{\"id\":\"COM_LIMITADORES\",\"nome\":\"Com Limitadores\"},\"minimo\":\"-3\",\"maximo\":\"3\"},\"energia\":{\"id\":\"CONVENCIONAL\",\"nome\":\"Convencional\"},\"descontoTUSD\":\"Sem desconto\"}],\"pdfPLD\":null,\"propostaId\":\"DV - V0001\",\"prazo\":{\"data\":\"08/07/2021\",\"hora\":\"12:31 h\"}}")
    with open('./templates/replaced.html', 'w') as w:
      w.write(replaced)

  options = Options()
  options.add_argument('--headless')
  options.add_argument('--disable-gpu')
  driver = webdriver.Chrome('./chromedriver/chromedriver', chrome_options=options)
  driver.get("http://0.0.0.0:5000/pdf")

  elem = driver.find_elements_by_tag_name("html")[0].get_attribute('innerHTML')
  with open('./templates/aaa.html', 'w') as w:
    w.write(elem)

  driver.quit()

  pdfkit.from_file('templates/aaa.html', 'out.pdf')
  return send_file("out.pdf")

@app.route('/pdf')
def pdf():
  return send_file('./templates/replaced.html')


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
