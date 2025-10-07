# Problemas com valor de disco alto:

1. Limpe o arquivo de paginação

Pressione a combinação de teclas Windows + X;
Clique em Windows Powershell (Admin);
Em seguida, cole o seguinte comando para limpar automaticamente o arquivo de paginação ao desligar o computador: 
REG ADD /“HKLMSYSTEMCurrentControlSetControlSession ManagerMemory Management” /v ClearPageFileAtShutdown /t REG_DWORD /d 1 /f
Daí é só pressionar "Enter" para concluir o procedimento;
Com esse comando, seu computador limpará o arquivo de paginação sempre que você desligar seu PC.

2. Desative a opção Windows Search

Pressione a tecla "Windows";
Na barra de pesquisa, procure por "Serviços" e clique sobre a primeira opção;
Em seguida, procure pelo componente "Windows Search" e dê um duplo clique sobre ela;
Feito isso, clique em parar e depois selecione a opção "Desativado" na categoria "Tipo de inicialização";
Por fim, clique em "Aplicar" e em "Ok" para concluir a configuração.

3. Limite tarefas do Windows Schedule

Pressione o comando Windows + R;
Então digite "regedit" e aperte a tecla "Enter";
Clique duas vezes na pasta HKEY_LOCAL_MACHINE;
Acesse a pasta "SYSTEM";
Depois "CurrentControlSet";
Então clique na pasta "Services";
Por fim, acesse "Schedule";
Daí é só dar um duplo clique no registro "Start" e alterar o valor desse item de 2 para 4.
Essa configuração, limitará todas as tarefas agendadas do Windows, assim algumas delas não serão executadas e o consumo de disco pode voltar ao normal. Para concluir as alterações reinicie seu PC.

4. Desabilite softwares de terceiros na inicialização

Pressione a combinação de teclas Windows + R para ativar o comando "Executar";
No "Menu Executar" digite "msconfig" e clique em "Ok";
Acesse a categoria "Serviços";
Em seguida, habilite a opção "Ocultar todos os serviços Microsoft" e clique em "Desativar tudo";
Daí é só clicar em "Aplicar e depois "Ok" para concluir.

5. Desfragmente sua unidade de disco

Pressione o comando "Windows + X";
Clique em "Gerenciamento de disco";
Selecione seu disco principal e clique em "Propriedades";
Em seguida, acesse a categoria "Ferramentas" e depois clique em "Otimizar";
Daí você pode desfragmentar seu disco resolvendo problemas e tornando ele mais eficiente.