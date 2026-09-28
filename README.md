# Consulta de salário-maternidade

Roteiro de consulta para celular usado no **Projeto de Prática Extensionista em Seguridade Social** (Curso de Direito, Universidade Presbiteriana Mackenzie), de João Henrique Abrantes Camargo.

A página faz algumas perguntas sobre a situação de trabalho e contribuição da interessada e indica se há provável direito ao salário-maternidade, quais documentos reunir, onde fazer o pedido e quais prazos observar. Também sinaliza outros benefícios e as vias assistenciais.

## Como funciona

- É um único arquivo, `index.html`, sem servidor e sem banco de dados.
- As respostas ficam só na memória do navegador: nada é salvo, enviado ou coletado (LGPD, Lei 13.709/2018).
- Cada orientação exibida cita uma regra do quadro de requisitos (R01 a R27), com o fundamento legal. O quadro completo aparece no botão **"Ver as regras"**.

## Aviso

Orientação de caráter geral. Não substitui o atendimento pelo INSS, pela Defensoria Pública ou por profissional habilitado.

## Folder impresso

A pasta `folder/` tem o folder trifold (A4 paisagem, frente e verso) com o QR code que leva a esta página.

- `folder.html`: layout do folder
- `build.py`: gera o PDF (`pip install playwright qrcode` e depois `python build.py "URL-DA-PÁGINA"`)
- `Folder_Salario-Maternidade.pdf`: versão pronta para impressão
