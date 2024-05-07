from markmoji import handlers


class AltmetricHandler(handlers.MarkmojiHandler):
    """
    Handler for an altmetric citation.

    ### Parameters
    label (str)
    :    Text citation

    link (str)
    :    DOI link (if any)
    """
    # Volleyball emoji, because it looks a bit like the altmetric doughnuts
    emoji = "🏐"
    requirements = "<script type='text/javascript' src='https://d1bxh8uas1mnw7.cloudfront.net/assets/embed.js'></script>"

    example = "🏐[Mather, G., Sharman, R. J., & Parsons, T. (2017). Visual adaptation alters the apparent speed of real-world actions. <i>Scientific reports, 7</i>(1), 1-10.](10.1038/s41598-017-06841-5)"
    __author__ = "🦊"

    @property
    def html(self):
        return f"<div class='altmetric-citation'{self.html_params}><div class='altmetric-embed' data-badge-type='donut' data-doi='{self.link}'></div><a href=https://doi.org/{self.link}>{self.label}</a></div>"
