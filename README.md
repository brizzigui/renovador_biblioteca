# renovador_biblioteca

Esta ferramenta permite automatizar a renovação dos livros retirados nas Bibliotecas da UFSM.
(This tool makes it possible to automate book lease renewals of books taken from UFSM's libraries.)

### Tutorial
(**passo 0:** caso ainda não tenha uma conta no GitHub, [crie sua conta](https://github.com/signup).)
  
**1º passo:** clique em fork para copiar o repositório. Agora, você terá uma cópia do repositório associada à sua conta.  
**2º passo:** vá em "Settings" e, sob a seção "Security", clique em "Secrets and variables" e depois em "Actions".  
**3º passo:** clique em "New repository secret".  
**4º passo:** em "Name", digite "USER". E, no campo "Secret", digite sua matrícula. Depois, clique em "Add secret".  
**5º passo:** clique novamente em "New repository secret". Agora, no campo "Name", digite "SENHA" e, no campo "Secret", digite a sua senha. Clique em "Add secret". (Não se preocupe, as suas informações não serão compartilhadas e continuarão privadas mesmo mantendo o repositório como público.)  
**6º passo:** clique em "Actions" e reative os workflows. Se você quiser, clique em "Run workflow" para testar o funcionamento.

### Como funciona?
Usa um script em python com a biblioteca Selenium para entrar no site, realizar o login do usuário e renovar os livros que estão na data ideal de renovação.


