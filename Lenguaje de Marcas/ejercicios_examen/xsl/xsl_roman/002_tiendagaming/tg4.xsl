<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

  <xsl:output method="html" encoding="UTF-8" indent="yes"/>

  <xsl:template match="/tiendaGaming">
    <html>
      <head>
        <title>Productos en <xsl:value-of select="@nombre"/></title>
      </head>
      <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f5f5f5;
            margin: 20px;
        }
        
        h1 {
            color: #333;
            text-align: center;
        }
        
        ul {
            list-style-type: none;
            padding: 0;
        }
        
        li {
            background-color: #fff;
            margin-bottom: 15px;
            padding: 15px;
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }
        
        strong {
            font-size: 1.2em;
        }
        
        span {
            display: block;
            margin-top: 5px;
        }
        
      </style>
      <body>
        <h1>Productos en <xsl:value-of select="@nombre"/></h1>
        <ul>
          <xsl:for-each select="producto">
            <li>
              <strong><xsl:value-of select="nombre"/></strong> -
              <xsl:value-of select="marca"/>:
              <xsl:value-of select="precio"/> €
              <br/>
              <xsl:choose>
                <xsl:when test="stock/@disponible = 'sí' and stock &gt; 0">
                  <span style="color: green;">En stock: <xsl:value-of select="stock"/> unidades</span>
                </xsl:when>
                <xsl:otherwise>
                  <span style="color: red;">No disponible</span>
                </xsl:otherwise>
              </xsl:choose>
            </li>
          </xsl:for-each>
        </ul>
      </body>
    </html>
  </xsl:template>

</xsl:stylesheet>
