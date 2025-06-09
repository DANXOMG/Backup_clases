<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="html" encoding="UTF-8"/>
    <xsl:template match="/tiendaGaming">
        <html>
            <head>
                <tittle>Productos sin stock</tittle>
                <style>
                    body {
                        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                        background-color: #f9f9f9;
                    }
                    h1 {
                        text-align: center;
                        color: #b30000;
                    }
                    table {
                        width: 80%;
                        margin: 20px auto;
                        border-collapse: collapse;
                        box-shadow: 0 0 10px rgba(0,0,0,0.1);
                    }
                    th, td {
                        border: 1px solid #ddd;
                        padding: 10px;
                        text-align: center;
                    }
                    th {
                        background-color: #b30000;
                        color: white;
                    }
                    tr:nth-child(even) {
                        background-color: #f2f2f2;
                    }
                </style>
            </head>
            <body>
                <h1>Productos sin stock</h1>
                <table>
                    <tr>
                        <td>Nombre</td>
                        <td>Marca</td>
                        <td>Precio</td>
                        <td>Stock</td>
                        <td>Disponible</td>
                        <td>Categoria</td>
                    </tr>
                    <xsl:for-each select="producto">
                        <xsl:choose>
                            <xsl:when test="number(stock) = 0">
                                <tr>
                                    <td><xsl:value-of select="nombre"/></td>
                                    <td><xsl:value-of select="marca"/></td>
                                    <td><xsl:value-of select="precio"/></td>
                                    <td><xsl:value-of select="stock"/></td>
                                    <td><xsl:value-of select="stock/@disponible"/></td>
                                    <td><xsl:value-of select="@categoria"/></td>
                                </tr>
                            </xsl:when>
                        </xsl:choose>
                    </xsl:for-each>
                </table>
            </body>
        </html>
    </xsl:template>

</xsl:stylesheet>
