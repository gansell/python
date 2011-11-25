<xsl:stylesheet  version='1.0'
     xmlns:xsl='http://www.w3.org/1999/XSL/Transform'>

    <xsl:key name="cityname" match="entry" use="city" />

    <xsl:template match="city">
        <xsl:variable name="name" select="." />
        <xsl:for-each select="document('../cityindex_attrs.xml')">
            <city inhabitants="{key('cityname', $name)/inhabitants[@year='2010']}">
                <xsl:value-of select="$name" />
            </city>
        </xsl:for-each>
    </xsl:template>

    <xsl:template match="*">
    	<xsl:copy>
            <xsl:copy-of select="@*" />
            <xsl:apply-templates />
        </xsl:copy>
    </xsl:template>
</xsl:stylesheet>
