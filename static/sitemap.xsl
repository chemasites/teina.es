<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  xmlns:sm="http://www.sitemaps.org/schemas/sitemap/0.9"
  xmlns:image="http://www.google.com/schemas/sitemap-image/1.1"
  xmlns:video="http://www.google.com/schemas/sitemap-video/1.1"
  exclude-result-prefixes="sm image video">

  <xsl:output method="html" version="1.0" encoding="UTF-8" indent="yes"/>

  <xsl:template match="/">
    <html lang="es">
      <head>
        <meta charset="UTF-8"/>
        <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
        <meta name="robots" content="noindex, follow"/>
        <title>Teína — Sitemap</title>
        <style>
          *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

          body {
            font-family: Georgia, serif;
            background-color: #f9f5f0;
            color: #3a3530;
            padding: 2rem 1rem;
            line-height: 1.6;
          }

          .container {
            max-width: 1000px;
            margin: 0 auto;
          }

          header {
            border-bottom: 2px solid #3a3530;
            padding-bottom: 1.25rem;
            margin-bottom: 2rem;
          }

          header h1 {
            font-size: 1.8rem;
            letter-spacing: 0.04em;
            margin-bottom: 0.35rem;
          }

          header p {
            font-size: 0.9rem;
            color: #6b5e52;
          }

          header a {
            color: #3a3530;
            text-decoration: underline;
            text-underline-offset: 3px;
          }

          header a:hover { color: #2a2520; }

          h2 {
            font-size: 1.1rem;
            letter-spacing: 0.06em;
            text-transform: uppercase;
            margin-bottom: 1rem;
            color: #2a2520;
          }

          section { margin-bottom: 2.5rem; }

          .stats {
            display: flex;
            gap: 2rem;
            margin-bottom: 2rem;
            flex-wrap: wrap;
          }

          .stat {
            background: #ede8e1;
            border: 1px solid #c8bdb4;
            border-radius: 4px;
            padding: 0.75rem 1.25rem;
            text-align: center;
            min-width: 120px;
          }

          .stat-number {
            display: block;
            font-size: 1.6rem;
            font-weight: bold;
            color: #2a2520;
          }

          .stat-label {
            font-size: 0.8rem;
            color: #6b5e52;
            letter-spacing: 0.04em;
            text-transform: uppercase;
          }

          table {
            width: 100%;
            border-collapse: collapse;
            font-size: 0.875rem;
          }

          thead th {
            background-color: #3a3530;
            color: #f9f5f0;
            text-align: left;
            padding: 0.6rem 0.75rem;
            letter-spacing: 0.04em;
            font-size: 0.8rem;
            text-transform: uppercase;
          }

          tbody tr:nth-child(odd)  { background-color: #f9f5f0; }
          tbody tr:nth-child(even) { background-color: #f0ebe4; }

          tbody tr:hover { background-color: #e4ddd5; }

          td {
            padding: 0.5rem 0.75rem;
            border-bottom: 1px solid #ddd5cc;
            word-break: break-all;
          }

          td a {
            color: #3a3530;
            text-decoration: none;
          }

          td a:hover {
            text-decoration: underline;
            text-underline-offset: 2px;
          }

          td.center { text-align: center; }

          .priority-high   { color: #2a6b2a; font-weight: bold; }
          .priority-mid    { color: #6b4a2a; }
          .priority-low    { color: #6b5e52; }

          .image-list {
            list-style: none;
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 0.75rem;
          }

          .image-list li {
            background: #ede8e1;
            border: 1px solid #c8bdb4;
            border-radius: 4px;
            padding: 0.6rem 0.9rem;
            font-size: 0.85rem;
            word-break: break-all;
          }

          .image-list li a {
            color: #2a2520;
            text-decoration: none;
          }

          .image-list li a:hover { text-decoration: underline; }

          footer {
            margin-top: 3rem;
            padding-top: 1rem;
            border-top: 1px solid #c8bdb4;
            font-size: 0.8rem;
            color: #6b5e52;
            text-align: center;
          }

          @media (max-width: 600px) {
            thead th:nth-child(3),
            thead th:nth-child(4),
            td:nth-child(3),
            td:nth-child(4) { display: none; }

            .stats { gap: 1rem; }
          }
        </style>
      </head>
      <body>
        <div class="container">
          <header>
            <h1>Teína — Sitemap</h1>
            <p>
              Mapa del sitio generado automáticamente.
              Visita <a href="https://teina.es/">teina.es</a> para ver la web.
            </p>
          </header>

          <!-- Stats -->
          <xsl:variable name="urlCount"   select="count(sm:urlset/sm:url)"/>
          <xsl:variable name="imageCount" select="count(sm:urlset/sm:url/image:image)"/>
          <xsl:variable name="videoCount" select="count(sm:urlset/sm:url/video:video)"/>

          <div class="stats">
            <div class="stat">
              <span class="stat-number"><xsl:value-of select="$urlCount"/></span>
              <span class="stat-label">URLs</span>
            </div>
            <xsl:if test="$imageCount &gt; 0">
              <div class="stat">
                <span class="stat-number"><xsl:value-of select="$imageCount"/></span>
                <span class="stat-label">Imágenes</span>
              </div>
            </xsl:if>
            <xsl:if test="$videoCount &gt; 0">
              <div class="stat">
                <span class="stat-number"><xsl:value-of select="$videoCount"/></span>
                <span class="stat-label">Vídeos</span>
              </div>
            </xsl:if>
          </div>

          <!-- URL table -->
          <section>
            <h2>URLs</h2>
            <table>
              <thead>
                <tr>
                  <th>URL</th>
                  <th>Última modificación</th>
                  <th>Frecuencia</th>
                  <th>Prioridad</th>
                </tr>
              </thead>
              <tbody>
                <xsl:for-each select="sm:urlset/sm:url">
                  <xsl:sort select="sm:priority" data-type="number" order="descending"/>
                  <tr>
                    <td>
                      <a href="{sm:loc}"><xsl:value-of select="sm:loc"/></a>
                    </td>
                    <td class="center"><xsl:value-of select="sm:lastmod"/></td>
                    <td class="center"><xsl:value-of select="sm:changefreq"/></td>
                    <td class="center">
                      <xsl:variable name="p" select="sm:priority"/>
                      <xsl:choose>
                        <xsl:when test="$p &gt;= 0.9">
                          <span class="priority-high"><xsl:value-of select="$p"/></span>
                        </xsl:when>
                        <xsl:when test="$p &gt;= 0.7">
                          <span class="priority-mid"><xsl:value-of select="$p"/></span>
                        </xsl:when>
                        <xsl:otherwise>
                          <span class="priority-low"><xsl:value-of select="$p"/></span>
                        </xsl:otherwise>
                      </xsl:choose>
                    </td>
                  </tr>
                </xsl:for-each>
              </tbody>
            </table>
          </section>

          <!-- Images section -->
          <xsl:if test="$imageCount &gt; 0">
            <section>
              <h2>Imágenes (<xsl:value-of select="$imageCount"/>)</h2>
              <ul class="image-list">
                <xsl:for-each select="sm:urlset/sm:url/image:image">
                  <li>
                    <a href="{image:loc}"><xsl:value-of select="image:loc"/></a>
                    <xsl:if test="image:title">
                      <br/><small><xsl:value-of select="image:title"/></small>
                    </xsl:if>
                  </li>
                </xsl:for-each>
              </ul>
            </section>
          </xsl:if>

          <!-- Videos section -->
          <xsl:if test="$videoCount &gt; 0">
            <section>
              <h2>Vídeos (<xsl:value-of select="$videoCount"/>)</h2>
              <ul class="image-list">
                <xsl:for-each select="sm:urlset/sm:url/video:video">
                  <li>
                    <a href="{video:player_loc}"><xsl:value-of select="video:title"/></a>
                    <xsl:if test="video:description">
                      <br/><small><xsl:value-of select="video:description"/></small>
                    </xsl:if>
                  </li>
                </xsl:for-each>
              </ul>
            </section>
          </xsl:if>

          <footer>
            Este sitemap es procesado por motores de búsqueda para indexar teina.es.
          </footer>
        </div>
      </body>
    </html>
  </xsl:template>

</xsl:stylesheet>
