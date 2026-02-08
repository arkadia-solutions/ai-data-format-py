import sys
import textwrap
from .colors import C

# --- LOGO (Raw f-string fix) ---
def get_logo(color_accent=C.AID_ACCENT):
    return fr"""{color_accent}
                             :SB@MMWBZSr,
                         ,irXX7ri, iaBWMMMMM@a:    :,
                    i2WMMMMMMMMMMMM@a:7ZZWMMMMM@7 :i,02,
                 ,7S7;i::i;72Z2S0@ZZWMW;r7iBWWM@M2 rM0BM;
                   ia@@08Z0B2:  :,i0r rBZ,: XSBMZM: 2MMMMi
                 iBZ7i:,   iXZZSi   i;  ia   ;:@22: ;M@MMS
                 ,:    ,, ,7:  ,Xi  ;r,   :   ,SS,  rBZ8MiX7,
             r8WZ: XW@0Z8WMZ: rX: :M2;BZ ;r:   ;,   ::Si;ii   :7
          :8MM@a,:@0:      XM2  , i@WZMZ 28MMMBr     , :ZW@a  iB@;
        ,Z0MMWZi BB  ,aZ8i      S7,,  ;SXZMMMMMMMa::r ,         7M8,
        :;MMZ:   8Z  :07Z7   @X XaSa,:8MMMM2ZMMMMMMM@MS   i2 ,BX :WW:
        iM0:  ,X,i8r        XM:,S7a; XZWMMMM2,8MMMMMWr8M2, iS,    ,B@:
        87  iB0:,,,XZX,  XW S@    ,;aZ00ZZ2SX7,:S8082,iM00, :i  ar ,WW,
        : :0MB@Zi,,      iM2 Sr :;Xriirr:  ZM8      ,XBM@X   :   ,: i@a
         rMMMW0X:  8Z     : ;a00Z7,,2BMMWBZXi  :,   iaWMMMMB7    :;  2Wi
        rMMBr     ZW ,i   rW7a00Z702 78@MMMMMMMM0@MMM@@@MMMMMM0r     iWS
       :MZ,  ,7: ;M2;Zii,:MrB,   2S07 ZZ8BZ,XB0WMMMMMMMMW280BWWWW8i   8Z
       S:  ,ZZ   XMZW:rr, Z;B:  ,ZXSi S2222XXX7ZBZ;:BMMM@X:   irr:    ZZ
          ;MZ;   rMMX   : ,27XZZS;S;     ii    ,i,ZMMMMMMMMM@7  ,8Z   aa
         ;MM0: ,  BMi  iS   ,irr;:;, :7,,Wa S8Z,,aXMZWBBMMMMMMS:MM8  ,ZX
        ,WMM0,2   :@,  0rr        ;@Br2,7S ::r7,ir;rr8ZZMMMMMMSiMMa  ;ai
        rMMM8a7    ,:  @0:  ,:    ,   ,         ,Z222X77@MW02i iZW: ,SX
        X@SM0@:        BB   ;r   :S     ,;7XS77; ,XZZZZ82r, :;i ,,  ;X:
        ;riMMM:  , r , ;0 ,:7Z  ;SS   ;     ,       ,:  iZ@MMMMM2
           8MM;  ; Z ;i ;, XrMi  B8   X7 , ,7        ,XZWMMMMMM@B
           ,WM2  7;87:8    XXMW, ,Bi ;7@i i Z     ,;2aa8MWWMMMM02
            ,B@, :ZaMiBX   :ZBMWr, ;  XB@iiXX2::     Xa7;80Z@0a :
              X8  r8WMaMr   iZ0MM0,    ,X@;;ZWX8       :S; 7:
               ,i  rBWMMMr   :X;WM@r      ir:0@W0
                    ,0@MMM2    : ;BMWi        7@MW:
                      :0MMMWi       ;aBS:       i8MZ:
                         XBMMW;                    ,;r,
                            iS0@8;{C.RESET}"""

def print_banner(
    tool_name: str, 
    version: str, 
    color: str = C.AID_MAIN,
    description: str = "", 
    metadata: dict = None
):
    """
    Prints a standardized, responsive banner for Arkadia Tools.
    """
    # 1. Print Logo
    print(get_logo(color_accent=color))
    
    # 2. Print Header (Tool Name)
    # Arkadia prefix in Green, Tool name in White Bold
    print(f"\n\n   {C.AID_MAIN}Arkadia{C.RESET} {C.BOLD}{C.WHITE}{tool_name.upper()}{C.RESET}")
    print(f"   {C.DIM}{'-' * 50}{C.RESET}")

    # 3. Print Description (Wrapped)
    if description:
        # Wrap text to 60 chars for neatness, indented by 3 spaces
        wrapped = textwrap.fill(description, width=65)
        indented_desc = textwrap.indent(wrapped, "   ")
        print(f"{C.WHITE}{indented_desc}{C.RESET}\n")

    # 4. Print Metadata (Version, Model, Stats, etc.)
    # Format:  Label:    Value
    print(f"   {C.DIM}Version:{C.RESET} \t{C.YELLOW}{version}{C.RESET}")
    
    if metadata:
        for key, value in metadata.items():
            # Align keys if needed, but simple tab is usually fine
            print(f"   {C.DIM}{key}:{C.RESET} \t{C.CYAN}{value}{C.RESET}")

    print("\n") # Extra spacing at bottom