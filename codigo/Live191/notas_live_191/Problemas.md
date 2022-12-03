# Problemas

## Conflito de versões

Imagine que eu instalei uma vez a biblioteca Pandas para um projeto meu. Na época o Pandas estava na versão 1.4, e eu me utilizo dela para esse projeto. Depois de concluído o projeto, eu parto para um próximo, onde eu também preciso do Pandas, mas como ele foi atualizado pra versão 2.0 nesse meio tempo, preciso reinstalar ele. Quando eu pedir pro **gerenciador de pacotes** atualizar a versão, ela vai ser instalada na mesma pasta **global**, sobrescrevendo a versão 1.4, e isso pode fazer com que o meu projeto antigo quebre. Bom, então basta eu usar a versão 1.4 no novo projeto, certo? Você pode fazer isso, sim. Mas e se a versão 2.0 do pacote adicionou uma funcionalidade ótima que você gostaria de usar? Como eu faço? Instalo ambas as versões? Será que isso é possível? Talvez, mas existem soluções melhores. Antes, vejamos outra situação onde pacotes podem nos causar problemas.

## O inferno de dependencias

Imagine que alguém instalou o pacote `httpx`. Ele depende de algumas outras bibliotecas, como o `httpcore`, e em versoes específicas. Depois, essa pessoa instala outra biblioteca que também depende do pacote `httpcore`, mas em uma outra versão que é incompatível com a versão da qual o `httpx` depende. Então temos aqui um **conflito de versões**.

Quando instalamos todas as bibliotecas globalmente, o conflito de versões se torna cada vez mais provável conforme vamos instalando cada vez mais pacotes. Então, como é que fazemos pra solucionar esses problemas?

Utilizando **ambientes virtuais**!
