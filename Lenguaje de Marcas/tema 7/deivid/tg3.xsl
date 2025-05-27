<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

    <xsl:output method="html"/>
    <xsl:template match="/tiendagaming">
        <html>
            <head>
                <tittle>Productos de <xsl:value-of select ="@nombre"/></tittle>  
            </head>

            <style>
                body {
                    font-family: Arial;
                    background-color: #f9f9f9;
                    padding: 20px;
                }
                h2 {
                    color: #333;
                }
                table {
                    border-collapse: collapse;
                    width: 100%;
                    margin-botton: 30px;
                }
                th,td{
                    border: 1px solid #333;
                    background-color: #f2f2f2;
                    padding: 8px;
                    color: black;
                }
                th {
                    background-color: green;;
                    color: azure;
                }
                h1 {
                    color: blue;

                }

            </style>
            
            <body>
                <h1>Productos de la tienda <xsl:value-of select ="@nombre"/></h1>
                <h2>Productos con precio mayor o igual a 100 Euros</h2>
                <table>
                    <tr>
                        <th>Nombre</th>
                        <th>Marca</th>
                        <th>Precio</th>
                        <th>Categoria</th>
                    </tr>
                    <xsl:apply-templates select="producto[number(precio) &gt;= 100]"/>
                </table>


                <h2>Productos con precio menor a 100 Euros</h2>
                <table>
                    <tr>
                        <th>Nombre</th>
                        <th>Marca</th>
                        <th>Precio</th>
                        <th>Categoria</th>
                    </tr>
                    <xsl:apply-templates select="producto[number(precio) &lt; 100]"/>
                </table>

                <h2>Productos agotados</h2>
                <table>
                    <tr>
                        <th>Nombre</th>
                        <th>Marca</th>
                        <th>Precio</th>
                        <th>Categoria</th>
                    </tr>
                    <xsl:apply-templates select="producto[stock = 0]"/>
                </table>

                <h2>Productos de categoria Teclado</h2>
                <table>
                    <tr>
                        <th>Nombre</th>
                        <th>Marca</th>
                    </tr>
                    <xsl:apply-templates select="producto[@categoria = 'teclado']"/>
                </table>
            </body>
        </html>

    </xsl:template>

    <xsl:template match="producto">
            <tr>
                <td><xsl:value-of select="nombre"/></td>
                <td><xsl:value-of select="marca"/></td>
                <td><xsl:value-of select="precio"/></td>
                <td><xsl:value-of select="@categoria"/></td>
            </tr>
    </xsl:template>

    <xsl:template match="producto[@categoria = 'teclado']">
            <tr>
                <td><xsl:value-of select="nombre"/></td>
                <td><xsl:value-of select="marca"/></td>
            </tr>
    </xsl:template>

   
</xsl:stylesheet>