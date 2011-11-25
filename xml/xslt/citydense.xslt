<xsl:stylesheet  version='1.0'
     xmlns:xsl='http://www.w3.org/1999/XSL/Transform'>

  <xsl:template match="/cityindex">
    <dense-cities>
      <title>The 10 most densely populated major German cities</title>

      <!-- select and sort all entry elements -->
      <xsl:for-each select="entry">
        <xsl:sort select="inhabitants_per_km2"
                  data-type="number"
                  order="descending" />

        <!-- process top 10 elements -->
        <xsl:if test="position() &lt;= 10">
          <name density="{inhabitants_per_km2}">
            <xsl:value-of select="city" />
          </name>
        </xsl:if>
      </xsl:for-each>

    </dense-cities>
  </xsl:template>
</xsl:stylesheet>
