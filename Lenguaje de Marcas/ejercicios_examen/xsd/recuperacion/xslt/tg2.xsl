<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="html" encoding="UTF-8"/>
    <xsl:template match="/tiendaGaming">
        <html>
            <head>
                <tittle>Productos Gaming mayor de 100$</tittle>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        background-color: #f8f8f8;
                    }
                    h1 {
                        text-align: center;
                        color: #222;
                    }
                    table {
                        width: 80%;
                        margin: 20px auto;
                        border-collapse: collapse;
                        box-shadow: 0 0 10px rgba(0,0,0,0.1);
                    }
                    th, td {
                        border: 1px solid #ccc;
                        padding: 12px;
                        text-align: center;
                    }
                    th {
                        background-color: #222;
                        color: #fff;
                    }
                    tr:nth-child(even) {
                        background-color: #eee;
                    }
                </style>
            </head>
            <body>
                <h1>Productos Gaming mayor de 100$</h1>
                <table>
                    <tr>
                        <td>Nombre</td>
                        <td>Marca</td>
                        <td>Precio</td>
                        <td>Stock</td>
                        <td>Categoria</td>
                    </tr>
                    <xsl:for-each select="producto[number(precio) &gt; 100]">
                        <tr>
                            <td><xsl:value-of select="nombre"/></td>
                            <td><xsl:value-of select="marca"/></td>
                            <td><xsl:value-of select="precio"/></td>
                            <td><xsl:value-of select="stock"/></td>
                            <td><xsl:value-of select="@categoria"/></td>
                        </tr>
                    </xsl:for-each>
                </table>
            </body>
        </html>

    </xsl:template>
</xsl:stylesheet>