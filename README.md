<h1 > NorthWind DB </h1>
<h2 > Primeiros studos sobre os serviços AWS usando o banco de dados educacional NorthWind, cedido pela Microsoft.</h2>

<h3>O NorthWind DB é um arquivo público; neste projeto utilizei uma variação do mesmo, onde a tabela "order_details" se encontra num arquivo CSV isolado.</h3>

<h4> 
	 Em processo de construção...  🚧
</h4>

A seguir apresento os arquivos presentes, a intenção pretendida com eles, e estado de funcionamento atual.

<ol>
  <li> <strong> extractor.py </strong> </li>
    função: busca as tabelas do NorthWind presentes no PostGre SQL; estabelece relações entre as diferentes tabelas de acordo com PRIMARY_KEYS e FOREIGN_KEYS, extrai a informação de cada uma delas de acordo com o nome da tabela e o dia em que ocorreu um determinado pedido selecionado;
  estado: funcionando perfeitamente
  <li> <strong> loader.py</strong></li>
   função: Utiliza as tabelas extraidas do banco de dados original, e carrega os mesmos no serviço s3 da AWS utilizando o Python SDK (boto3);    
  estado: funcionando (os arquivos estão públicos, no bucket de 'arn:aws:s3:::indicium-challenge')
  <li><strong> index.html</strong> </li>
    função Arquivo para geração de um website estatico, onde um usuario escolhe um data dentro do intervalo dos pedidos presente no s3; após este procedimento, o servidor é acionado e retora os arquivos JSON envolvidos.
    estado: ocorrendo erro de autenticação
 </ol>
