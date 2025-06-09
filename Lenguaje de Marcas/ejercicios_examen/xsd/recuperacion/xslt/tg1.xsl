<?xml version="1.0" encoding="UTF-8"?>

<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

    <xsl:output method="html" encoding="UTF-8" indent="yes"/> <!--Metodo de salida del xml a html-->
    <xsl:template match="/tiendaGaming">
        <html>
            <head>
                <tittle>Tienda Gaming</tittle>
                <style>
                    table {
                        width: 80%;
                        margin: 20px auto;
                        border-collapse: collapse;
                        font-family: Arial, sans-serif;
                    }
                    th, td {
                    border: 1px solid #ccc;
                    padding: 10px;
                    text-align: center;
                    }
                    th {
                        background-color: #333;
                        color: white;
                    }
                    tr:nth-child(even) {
                    background-color: #f2f2f2;
                    }
                    h1 {
                    text-align: center;
                    font-family: Verdana, sans-serif;
                    color: #444;
                    }
                </style>
            </head>
            <body>
                <h1>Productos por menos de 100$</h1>
                <table>
                    <tr>
                        <th>Nombre</th>
                        <th>Marca</th>
                        <th>Precio</th>
                        <th>Stock</th>
                        <th>Categoria</th>
                    </tr>
                    <xsl:for-each select="producto[number(precio) &lt; 100]">
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