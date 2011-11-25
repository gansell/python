<xsl:stylesheet  version='1.0'
     xmlns:xsl='http://www.w3.org/1999/XSL/Transform'>

  <xsl:template match="/cityindex">
    <xsl:copy>
      <!-- whitelist: handle only entry elements -->
      <xsl:apply-templates select="entry" />
    </xsl:copy>
  </xsl:template>

  <!-- blacklist: do nothing for matching elements -->
  <xsl:template match="inhabitants[@year='1990' or @year='2009']" />
  <xsl:template match="area_km2" />
  <xsl:template match="*[ contains(local-name(), 'development') ]" />

  <!-- wildcard fallback: deep copy all elements by default -->
  <xsl:template match="*">
    <xsl:copy>
      <xsl:copy-of select="@*" />
      <xsl:apply-templates />
    </xsl:copy>
  </xsl:template>
</xsl:stylesheet>
