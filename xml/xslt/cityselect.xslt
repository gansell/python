<xsl:stylesheet  version='1.0'
        xmlns:xsl='http://www.w3.org/1999/XSL/Transform'>

    <xsl:template match="/cityindex">
        <xsl:copy>
            <xsl:apply-templates select="entry" />
        </xsl:copy>
    </xsl:template>

    <xsl:template match="entry[ inhabitants_per_km2 &gt; 3000 ]">
        <xsl:copy-of select="." />
    </xsl:template>

    <xsl:template match="entry" />
</xsl:stylesheet>
