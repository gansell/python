<xsl:stylesheet  version='1.0'
        xmlns:xsl='http://www.w3.org/1999/XSL/Transform'>

    <xsl:output method="xml" encoding="UTF8" />

    <xsl:key name="cityindex" match="/*/entry" use="concat(city,'**',country)" />

    <xsl:template match="city">
    	<xsl:copy-of select="." />
        <xsl:variable name="key" select="concat(., '**', following-sibling::country)" />
    	<region>
            <xsl:for-each select="document('../cityindex.xml')">
                <xsl:value-of select="key('cityindex', $key)/region" />
            </xsl:for-each>
        </region>
    </xsl:template>

    <xsl:template match="*">
    	<xsl:copy>
            <xsl:copy-of select="@*" />
            <xsl:apply-templates />
        </xsl:copy>
    </xsl:template>

</xsl:stylesheet>
