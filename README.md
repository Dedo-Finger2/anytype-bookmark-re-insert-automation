## Anytype Bookmark re-insert

Este projeto se consiste numa ferramenta utilitária que vai pegar todos os bookmarks do seu Anytype
que estão sem nome e registrar eles novamente usando o novo Web Clipper oficial do AnyType.

### Porque usar este sistema?

Atualmente (26/03/2024) o Anytype está passando por alguns bugs relacionados a extração de dados
de links, principalmente do Youtube. Os bookmarks deste website agora vem:
- Sem nome;
- Sem descrição;
- Sem ícone;
- Sem imagem de fundo;

E isso é deverás frustrante, mas, por alguma razão o Web Clipper feito por eles consegue resolver
grande parte desses problemas, apenas deixando estes pendentes:
- Sem descrição;
- Sem imagem de fundo;
E se você salva mídias que consome no seu smartphone deve ter notado que ao compartilhar com o APP
oficial do AnyType o seu bookmark vem exatamente como foi descrito anteriormente, sem nome, descrição, etc...

Com essa automação você pode deixar o trabalho chato de usar o Web Clipper em cada uma das mídias salvas
nos seuss bookmarks, deixando eles mais corretos: com título do vídeo e o ícone.

### Como usar?

1. Deixe seu AnyType aberto;
2. Faça o pareamento entre o Web Clipper e o AnyType antes de rodar o script;
3. Certifique-se que a extensão está fixada no navegador;
4. Instale as dependências necessárias;
5. Não mova seu mouse nem seu teclado até ver o alerta na sua sua tela;
6. Após rodar o script você vai ter 5 segundos para voltar para o AnyType;
7. Deixe o AnyType em tela cheia;
8. Certifique-se de que o nome do seu Set de bookmarks se chama "Bookmarks".

### Dependências

- pyautogui;
    ```bash
    pip install pyautogui
    ```
- pyperclip;
    ```bash
    pip install pyperclip
    ```