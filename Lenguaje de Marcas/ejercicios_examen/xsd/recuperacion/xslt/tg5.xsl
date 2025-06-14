<?xml version="1.0" encoding="UTF-8"?>

<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="html" encoding="UTF-8" indent="yes"/>
    <xsl:template match="/tiendaGaming">
        <html>
            <head>
                <tittle>Tienda <xsl:value-of select="@nombre"/> </tittle>
                <style type="text/css">
                    body {
                        font-family: Verdana, sans-serif;
                        background-color: #f0f0f8;
                        padding: 20px;
                    }
                    h1 {
                        text-align: center;
                        color: #444;
                    }
                    .producto {
                        border: 1px solid #ccc;
                        padding: 15px;
                        margin-bottom: 10px;
                        background-color: #fff;
                        border-radius: 6px;
                    }
                    .disponible {
                        color: green;
                        font-weight: bold;
                    }
                    .nodisponible {
                        color: red;
                        font-style: italic;
                    }
                    .aviso {
                        background-color: #ffeeba;
                        padding: 5px;
                        border-left: 4px solid orange;
                        margin-top: 5px;
                    }
                </style>
            </head>
            <body>
                <h1>Productos disponibles en <xsl:value-of select="@nombre"/></h1>

                <xsl:for-each select="producto">
                    <xsl:value-of select="nombre"></xsl:value-of> (<xsl:value-of select="@categoria"></xsl:value-of>)
                    <br/>
                    Marca: <xsl:value-of select="marca"/>
                    <br/>
                    Precio: <xsl:value-of select="precio"/> $
                    <br/>

                    <br/>
                    <br/>

                    <xsl:choose>
                        <xsl:when test="stock/@disponible = sí and number(stock) &gt; 0">
                         <span class="disponible">Disponible: <xsl:value-of select="stock"/> unidades</span>
                        </xsl:when>
                        <xsl:otherwise>
                            <span class="nodisponible">No disponible</span>
                            
                        </xsl:otherwise>
                    </xsl:choose>

                    <!--Categoria = 'raton' o el precio > 200-->
                    <xsl:if test="producto/@categoria = 'raton' or number(precio) &gt; 200">
                        <div class="aviso">⚠ Producto especial: categoría popular o precio elevado</div>

                    </xsl:if>









                </xsl:for-each>

            </body>
        </html>

    </xsl:template>
</xsl:stylesheet>