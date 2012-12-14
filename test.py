from xml.dom.minidom import parse, parseString, getDOMImplementation

string = '<presence from="etmail10@gmail.com/androidf2c8ff57443f" to="james.wu.jimmy@gmail.com/0FD4FCA5" xmlns:stream="http://etherx.jabber.org/streams"><status>http://www.youtube.com/watch?v=xyqQ4iT4IeU&amp;feature=share&amp;list=UU1l7wYrva1qCH-wgqcHaaRg</status><priority>24</priority><caps:c node="http://www.android.com/gtalk/client/caps" ext="pmuc-v1 voice-v1 video-v1 camera-v1" ver="1.1" xmlns:caps="http://jabber.org/protocol/caps"/><show>away</show><x xmlns="vcard-temp:x:update"><photo>2f25a6be2398c202693ba67ba6a90a16aab901e3</photo></x></presence>'

proc = parseString(string)
inner = proc.getElementsByTagName("photo")[0].firstChild

#print string
print inner
print inner.nodeValue
print inner.nodeName
print inner.data

#print impl
#print newdoc

#print proc.getAttribute("body")
