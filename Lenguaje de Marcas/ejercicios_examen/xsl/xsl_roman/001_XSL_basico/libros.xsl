<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="html"/>
    <xsl:template match="/"> 
        <html>
            <head>
                <title>Libros Favoritos</title>
            </head>
            <style>
          th{color:white;
            background-color:blue;
            padding: 5px;
          }
             tr{
            text-align: center;
          }
          td{
            padding: 5px;
            border: 1px solid black;
          }
         table{
            border: 3px solid green;
         }
            </style>
            <body>
                <h2>Listas de libros Favoritos</h2>
                <table border="2">
                    <tr>
                        <th>TÍTULO</th>
                        <th>AUTOR</th>
                        <th>FECHA NACIMIENTO</th>
                        <th>AÑO PUBLICACIÓN</th>                        
                    </tr>
                    <xsl:for-each select="//libro">
                        <tr>
                            <td><xsl:value-of select="titulo"></xsl:value-of></td>
                            <td><xsl:value-of select="autor"></xsl:value-of></td>
                            <td><xsl:value-of select="autor/@fecha_nacimiento"></xsl:value-of></td>
                            <td><xsl:value-of select="fecha_publicacion/@año"></xsl:value-of></td>
                        </tr>
                    </xsl:for-each>
                </table>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>