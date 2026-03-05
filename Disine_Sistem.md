{
  "designSystem": {
    "meta": {
      "source": "3 iOS-экрана трекера гидратации (onboarding/логирование/статистика)",
      "platform": "iOS",
      "styleKeywords": ["clean", "aquatic", "soft-gradients", "glassmorphism-lite", "rounded-cards", "wave-illustrations"],
      "density": "comfortable",
      "notes": [
        "Основная визуальная идея: вода/волны + мягкие голубые градиенты.",
        "Компоненты выглядят iOS-native: SF-шрифт, большие скругления, мягкие тени.",
        "Наблюдаемые доминантные цвета (из изображения): #EAF2F8, #ABD2E7, #98B9D7, #1598D5, #0579C4, #68DCF2, #116BA7, #2BD0F3, #9DA2A9, #252631."
      ]
    },
    "colorPalette": {
      "primary": {
        "50": "#EAF2F8",
        "100": "#ABD2E7",
        "200": "#98B9D7",
        "300": "#5FADD4",
        "400": "#1598D5",
        "500": "#1598D5",
        "600": "#0579C4",
        "700": "#116BA7",
        "800": "#0B4F7A",
        "900": "#083753"
      },
      "secondary": {
        "50": "#F0FCFF",
        "100": "#C9F4FC",
        "200": "#A0ECF8",
        "300": "#68DCF2",
        "400": "#43D0F3",
        "500": "#2BD0F3",
        "600": "#14B9DE",
        "700": "#0D93B2",
        "800": "#086B82",
        "900": "#044B5A"
      },
      "neutral": {
        "0": "#FFFFFF",
        "50": "#F5FBFF",
        "100": "#EAF2F8",
        "200": "#D7EAF5",
        "300": "#C3DDEC",
        "400": "#ABD2E7",
        "500": "#9DA2A9",
        "600": "#7E8793",
        "700": "#5A6170",
        "800": "#3A3E4C",
        "900": "#252631"
      },
      "semantic": {
        "success": "#22C55E",
        "warning": "#F59E0B",
        "error": "#EF4444",
        "info": "#1598D5"
      },
      "background": {
        "primary": "#FFFFFF",
        "secondary": "#F5FBFF",
        "surface": "#FFFFFF",
        "surfaceMuted": "#EAF2F8",
        "overlay": "rgba(37,38,49,0.35)"
      },
      "gradients": {
        "aquaHero": {
          "type": "linear",
          "angle": 135,
          "stops": [
            { "color": "#EAF2F8", "position": 0 },
            { "color": "#ABD2E7", "position": 45 },
            { "color": "#1598D5", "position": 100 }
          ]
        },
        "waterWave": {
          "type": "linear",
          "angle": 180,
          "stops": [
            { "color": "rgba(104,220,242,0.55)", "position": 0 },
            { "color": "rgba(21,152,213,0.35)", "position": 55 },
            { "color": "rgba(5,121,196,0.18)", "position": 100 }
          ]
        },
        "progressRing": {
          "type": "conic",
          "stops": [
            { "color": "#0579C4", "position": 0 },
            { "color": "#1598D5", "position": 70 },
            { "color": "#68DCF2", "position": 100 }
          ]
        }
      }
    },
    "typography": {
      "fontFamilies": {
        "primary": "SF Pro Display",
        "secondary": "SF Pro Text",
        "monospace": "SF Mono"
      },
      "fontSizes": {
        "2xs": "10px",
        "xs": "12px",
        "sm": "14px",
        "base": "16px",
        "lg": "18px",
        "xl": "20px",
        "2xl": "24px",
        "3xl": "30px",
        "4xl": "36px"
      },
      "lineHeights": {
        "tight": "1.15",
        "normal": "1.4",
        "relaxed": "1.65"
      },
      "fontWeights": {
        "light": "300",
        "normal": "400",
        "medium": "500",
        "semibold": "600",
        "bold": "700"
      },
      "letterSpacing": {
        "tight": "-0.2px",
        "normal": "0px",
        "wide": "0.2px"
      },
      "textStyles": {
        "h1": {
          "fontFamily": "SF Pro Display",
          "fontSize": "30px",
          "fontWeight": "700",
          "lineHeight": "1.15",
          "letterSpacing": "-0.2px",
          "color": "#252631"
        },
        "h2": {
          "fontFamily": "SF Pro Display",
          "fontSize": "24px",
          "fontWeight": "700",
          "lineHeight": "1.2",
          "letterSpacing": "-0.2px",
          "color": "#252631"
        },
        "h3": {
          "fontFamily": "SF Pro Display",
          "fontSize": "20px",
          "fontWeight": "600",
          "lineHeight": "1.25",
          "letterSpacing": "-0.1px",
          "color": "#252631"
        },
        "subtitle": {
          "fontFamily": "SF Pro Text",
          "fontSize": "14px",
          "fontWeight": "500",
          "lineHeight": "1.4",
          "letterSpacing": "0px",
          "color": "#5A6170"
        },
        "body": {
          "fontFamily": "SF Pro Text",
          "fontSize": "16px",
          "fontWeight": "400",
          "lineHeight": "1.4",
          "letterSpacing": "0px",
          "color": "#3A3E4C"
        },
        "caption": {
          "fontFamily": "SF Pro Text",
          "fontSize": "12px",
          "fontWeight": "400",
          "lineHeight": "1.35",
          "letterSpacing": "0px",
          "color": "#7E8793"
        },
        "tabLabel": {
          "fontFamily": "SF Pro Text",
          "fontSize": "10px",
          "fontWeight": "500",
          "lineHeight": "1.2",
          "letterSpacing": "0px",
          "color": "#7E8793"
        },
        "numericLarge": {
          "fontFamily": "SF Pro Display",
          "fontSize": "24px",
          "fontWeight": "700",
          "lineHeight": "1.1",
          "letterSpacing": "-0.2px",
          "color": "#252631"
        },
        "numericMedium": {
          "fontFamily": "SF Pro Display",
          "fontSize": "18px",
          "fontWeight": "600",
          "lineHeight": "1.15",
          "letterSpacing": "-0.1px",
          "color": "#252631"
        }
      }
    },
    "spacing": {
      "scale": "exponential",
      "baseUnit": "4px",
      "values": {
        "0": "0px",
        "1": "4px",
        "2": "8px",
        "3": "12px",
        "4": "16px",
        "5": "20px",
        "6": "24px",
        "7": "28px",
        "8": "32px",
        "9": "36px",
        "10": "40px",
        "12": "48px",
        "14": "56px",
        "16": "64px"
      },
      "screenPadding": {
        "horizontal": "20px",
        "vertical": "16px"
      },
      "cardPadding": {
        "sm": "12px",
        "md": "16px",
        "lg": "20px"
      }
    },
    "borderRadius": {
      "none": "0px",
      "xs": "6px",
      "sm": "10px",
      "md": "14px",
      "lg": "18px",
      "xl": "24px",
      "2xl": "28px",
      "full": "9999px"
    },
    "borders": {
      "widths": {
        "none": "0px",
        "hairline": "0.5px",
        "thin": "1px",
        "medium": "2px"
      },
      "colors": {
        "subtle": "rgba(171,210,231,0.55)",
        "default": "rgba(157,162,169,0.35)",
        "strong": "rgba(90,97,112,0.35)"
      }
    },
    "shadows": {
      "sm": "0px 2px 8px rgba(17,107,167,0.10)",
      "md": "0px 8px 20px rgba(17,107,167,0.12)",
      "lg": "0px 14px 34px rgba(17,107,167,0.16)",
      "xl": "0px 22px 50px rgba(17,107,167,0.18)",
      "floating": "0px 10px 24px rgba(5,121,196,0.22)"
    },
    "blurEffects": {
      "glassLight": {
        "backdropFilter": "blur(14px)",
        "backgroundColor": "rgba(255,255,255,0.72)",
        "border": "1px solid rgba(215,234,245,0.8)"
      }
    },
    "layout": {
      "grid": {
        "columns": 4,
        "gap": "16px",
        "maxWidth": "390px",
        "safeArea": {
          "top": "44px",
          "bottom": "34px"
        }
      },
      "containers": {
        "sm": "320px",
        "md": "375px",
        "lg": "390px",
        "xl": "428px"
      }
    },
    "animations": {
      "transitions": {
        "fast": "150ms cubic-bezier(0.2, 0.8, 0.2, 1)",
        "normal": "300ms cubic-bezier(0.2, 0.8, 0.2, 1)",
        "slow": "500ms cubic-bezier(0.2, 0.8, 0.2, 1)"
      },
      "commonEffects": [
        "Нажатие кнопок/карточек: scale(0.98) + уменьшение тени на 20% (150ms).",
        "Сегмент-контрол: плавное перемещение активной плашки (spring, ~300ms).",
        "Progress ring: анимация заполнения по дуге (500ms ease-out) + плавное перемещение маркера.",
        "FAB: лёгкий bounce при появлении/тапе (spring).",
        "Переход между вкладками таббара: fade+slideY(2px) для иконки/лейбла."
      ]
    },
    "iconography": {
      "style": "outline (iOS-like), single-color; активные элементы могут быть filled/duotone через фон",
      "strokeWidth": "1.5px",
      "defaultSize": "24px",
      "sizes": {
        "xs": "16px",
        "sm": "20px",
        "md": "24px",
        "lg": "28px"
      },
      "colors": {
        "primary": "#1598D5",
        "secondary": "#7E8793",
        "onPrimary": "#FFFFFF",
        "muted": "#9DA2A9"
      }
    },
    "components": {
      "button": {
        "base": {
          "fontFamily": "SF Pro Text",
          "fontWeight": "600",
          "borderRadius": "9999px",
          "minHeight": "44px",
          "iconSize": "20px",
          "gap": "8px",
          "transition": "150ms cubic-bezier(0.2, 0.8, 0.2, 1)"
        },
        "variants": {
          "primary": {
            "backgroundColor": "#1598D5",
            "color": "#FFFFFF",
            "border": "0px",
            "shadow": "0px 10px 24px rgba(5,121,196,0.22)",
            "states": {
              "hover": {
                "backgroundColor": "#0579C4"
              },
              "active": {
                "transform": "scale(0.98)",
                "backgroundColor": "#0579C4",
                "shadow": "0px 6px 16px rgba(5,121,196,0.18)"
              },
              "disabled": {
                "backgroundColor": "rgba(21,152,213,0.35)",
                "color": "rgba(255,255,255,0.8)"
              },
              "focus": {
                "outline": "3px solid rgba(104,220,242,0.65)",
                "outlineOffset": "2px"
              }
            }
          },
          "secondary": {
            "backgroundColor": "#EAF2F8",
            "color": "#116BA7",
            "border": "1px solid rgba(171,210,231,0.65)",
            "shadow": "0px 2px 8px rgba(17,107,167,0.10)",
            "states": {
              "hover": {
                "backgroundColor": "#D7EAF5"
              },
              "active": {
                "transform": "scale(0.98)",
                "backgroundColor": "#C3DDEC"
              },
              "disabled": {
                "backgroundColor": "rgba(234,242,248,0.6)",
                "color": "rgba(17,107,167,0.35)"
              },
              "focus": {
                "outline": "3px solid rgba(104,220,242,0.55)",
                "outlineOffset": "2px"
              }
            }
          },
          "outline": {
            "backgroundColor": "transparent",
            "color": "#1598D5",
            "border": "1px solid rgba(21,152,213,0.55)",
            "shadow": "none",
            "states": {
              "hover": {
                "backgroundColor": "rgba(21,152,213,0.08)"
              },
              "active": {
                "transform": "scale(0.98)",
                "backgroundColor": "rgba(21,152,213,0.12)"
              },
              "disabled": {
                "border": "1px solid rgba(21,152,213,0.25)",
                "color": "rgba(21,152,213,0.35)"
              },
              "focus": {
                "outline": "3px solid rgba(104,220,242,0.55)",
                "outlineOffset": "2px"
              }
            }
          },
          "iconCircle": {
            "backgroundColor": "rgba(255,255,255,0.9)",
            "color": "#1598D5",
            "border": "1px solid rgba(215,234,245,0.8)",
            "borderRadius": "9999px",
            "shadow": "0px 8px 20px rgba(17,107,167,0.12)",
            "states": {
              "hover": { "backgroundColor": "#FFFFFF" },
              "active": { "transform": "scale(0.96)", "shadow": "0px 6px 16px rgba(17,107,167,0.10)" },
              "disabled": { "opacity": "0.45" },
              "focus": { "outline": "3px solid rgba(104,220,242,0.55)", "outlineOffset": "2px" }
            }
          }
        },
        "sizes": {
          "sm": {
            "minHeight": "36px",
            "padding": "8px 14px",
            "fontSize": "14px",
            "borderRadius": "9999px"
          },
          "md": {
            "minHeight": "44px",
            "padding": "10px 18px",
            "fontSize": "16px",
            "borderRadius": "9999px"
          },
          "lg": {
            "minHeight": "52px",
            "padding": "14px 22px",
            "fontSize": "18px",
            "borderRadius": "9999px"
          }
        }
      },
      "segmentedControl": {
        "base": {
          "height": "44px",
          "padding": "4px",
          "backgroundColor": "#FFFFFF",
          "border": "1px solid rgba(215,234,245,0.9)",
          "borderRadius": "9999px",
          "shadow": "0px 2px 8px rgba(17,107,167,0.10)"
        },
        "item": {
          "fontFamily": "SF Pro Text",
          "fontSize": "14px",
          "fontWeight": "600",
          "padding": "10px 16px",
          "borderRadius": "9999px",
          "states": {
            "active": {
              "backgroundColor": "#1598D5",
              "color": "#FFFFFF",
              "shadow": "0px 8px 20px rgba(5,121,196,0.16)"
            },
            "inactive": {
              "backgroundColor": "transparent",
              "color": "#7E8793"
            },
            "pressed": {
              "transform": "scale(0.98)"
            },
            "disabled": {
              "opacity": "0.45"
            }
          }
        },
        "motion": {
          "activePillTransition": "spring( stiffness: 380, damping: 30 )"
        }
      },
      "input": {
        "base": {
          "backgroundColor": "#FFFFFF",
          "border": "1px solid rgba(171,210,231,0.65)",
          "borderRadius": "14px",
          "padding": "12px 14px",
          "fontSize": "16px",
          "color": "#252631",
          "placeholder": {
            "color": "#9DA2A9",
            "opacity": "1"
          },
          "leadingIcon": {
            "size": "20px",
            "color": "#9DA2A9"
          },
          "states": {
            "focus": {
              "border": "1px solid rgba(21,152,213,0.85)",
              "shadow": "0px 0px 0px 4px rgba(104,220,242,0.35)"
            },
            "error": {
              "border": "1px solid rgba(239,68,68,0.85)",
              "shadow": "0px 0px 0px 4px rgba(239,68,68,0.15)"
            },
            "disabled": {
              "backgroundColor": "#EAF2F8",
              "color": "rgba(37,38,49,0.45)",
              "border": "1px solid rgba(171,210,231,0.35)"
            }
          }
        },
        "helperText": {
          "fontSize": "12px",
          "color": "#7E8793"
        }
      },
      "card": {
        "base": {
          "backgroundColor": "#FFFFFF",
          "border": "1px solid rgba(215,234,245,0.85)",
          "borderRadius": "24px",
          "padding": "16px",
          "boxShadow": "0px 8px 20px rgba(17,107,167,0.12)"
        },
        "variants": {
          "heroImage": {
            "borderRadius": "28px",
            "padding": "0px",
            "background": "linear-gradient(135deg, #EAF2F8 0%, #ABD2E7 45%, #1598D5 100%)",
            "contentOverlay": {
              "padding": "20px",
              "textColor": "#252631"
            }
          },
          "stats": {
            "borderRadius": "24px",
            "padding": "16px",
            "header": {
              "titleStyle": "h3",
              "rightControl": "dropdown"
            }
          },
          "miniTile": {
            "borderRadius": "18px",
            "padding": "12px",
            "minHeight": "88px",
            "backgroundColor": "#FFFFFF",
            "watermark": {
              "type": "wave",
              "opacity": "0.18",
              "color": "#1598D5"
            }
          }
        },
        "states": {
          "pressed": {
            "transform": "scale(0.99)",
            "boxShadow": "0px 6px 16px rgba(17,107,167,0.10)"
          }
        }
      },
      "navbar": {
        "topBar": {
          "height": "44px",
          "backgroundColor": "transparent",
          "title": {
            "textStyle": "subtitle",
            "alignment": "center",
            "color": "#252631"
          },
          "leftAction": {
            "type": "iconButton",
            "icon": "chevron-left",
            "size": "32px",
            "iconSize": "20px",
            "backgroundColor": "rgba(255,255,255,0.7)",
            "border": "1px solid rgba(215,234,245,0.8)",
            "borderRadius": "9999px",
            "shadow": "0px 2px 8px rgba(17,107,167,0.10)"
          },
          "rightAction": {
            "type": "iconButton",
            "icon": "share",
            "size": "32px",
            "iconSize": "20px",
            "backgroundColor": "rgba(255,255,255,0.7)",
            "border": "1px solid rgba(215,234,245,0.8)",
            "borderRadius": "9999px"
          }
        },
        "tabBar": {
          "height": "84px",
          "safeAreaBottom": "34px",
          "backgroundColor": "#FFFFFF",
          "borderTop": "1px solid rgba(215,234,245,0.95)",
          "shadow": "0px -8px 24px rgba(17,107,167,0.06)",
          "item": {
            "iconSize": "24px",
            "labelStyle": "tabLabel",
            "gap": "4px",
            "states": {
              "active": {
                "iconColor": "#1598D5",
                "labelColor": "#1598D5"
              },
              "inactive": {
                "iconColor": "#9DA2A9",
                "labelColor": "#7E8793"
              }
            }
          },
          "centerFABSlot": {
            "reservedWidth": "76px",
            "alignment": "center"
          }
        }
      },
      "fab": {
        "diamond": {
          "size": "56px",
          "shape": "square-rotated-45deg",
          "backgroundColor": "#1598D5",
          "borderRadius": "18px",
          "shadow": "0px 10px 24px rgba(5,121,196,0.22)",
          "icon": {
            "name": "droplet",
            "size": "24px",
            "color": "#FFFFFF"
          },
          "states": {
            "pressed": {
              "transform": "scale(0.96)",
              "backgroundColor": "#0579C4",
              "shadow": "0px 6px 16px rgba(5,121,196,0.18)"
            },
            "disabled": {
              "backgroundColor": "rgba(21,152,213,0.35)",
              "iconColor": "rgba(255,255,255,0.85)"
            }
          }
        }
      },
      "progress": {
        "circularRing": {
          "size": "240px",
          "track": {
            "color": "#D7EAF5",
            "strokeWidth": "18px",
            "lineCap": "round"
          },
          "progress": {
            "color": "#0579C4",
            "gradient": "conic(#0579C4 -> #1598D5 -> #68DCF2)",
            "strokeWidth": "18px",
            "lineCap": "round",
            "startAngle": "-90deg"
          },
          "thumbMarker": {
            "enabled": true,
            "size": "18px",
            "color": "#FFFFFF",
            "border": "3px solid #1598D5",
            "shadow": "0px 6px 16px rgba(17,107,167,0.14)"
          },
          "centerContent": {
            "titleStyle": "subtitle",
            "mainValueStyle": "numericLarge",
            "deltaStyle": {
              "fontFamily": "SF Pro Text",
              "fontSize": "14px",
              "fontWeight": "500",
              "color": "#7E8793"
            }
          },
          "motion": {
            "fillAnimation": "500ms ease-out",
            "thumbFollow": "500ms ease-out"
          }
        },
        "linear": {
          "height": "8px",
          "trackColor": "#D7EAF5",
          "fillColor": "#1598D5",
          "borderRadius": "9999px"
        }
      },
      "chart": {
        "bar": {
          "container": {
            "backgroundColor": "#FFFFFF",
            "borderRadius": "18px"
          },
          "grid": {
            "color": "rgba(171,210,231,0.55)",
            "strokeWidth": "1px",
            "style": "dashed",
            "dashPattern": "3 4"
          },
          "barStyle": {
            "width": "14px",
            "radius": "9999px",
            "color": "#1598D5",
            "inactiveOpacity": "0.35",
            "highlightedOpacity": "1"
          },
          "axis": {
            "labelStyle": "caption",
            "color": "#9DA2A9"
          },
          "interaction": {
            "tapHighlight": {
              "scaleY": "1.02",
              "shadow": "0px 8px 20px rgba(17,107,167,0.10)"
            },
            "tooltip": {
              "backgroundColor": "rgba(255,255,255,0.9)",
              "border": "1px solid rgba(215,234,245,0.9)",
              "borderRadius": "12px",
              "shadow": "0px 10px 24px rgba(17,107,167,0.12)",
              "textStyle": "caption"
            }
          }
        }
      },
      "dropdown": {
        "trigger": {
          "height": "32px",
          "padding": "6px 10px",
          "borderRadius": "9999px",
          "backgroundColor": "rgba(234,242,248,0.85)",
          "border": "1px solid rgba(215,234,245,0.9)",
          "textStyle": {
            "fontSize": "12px",
            "fontWeight": "600",
            "color": "#5A6170"
          },
          "icon": {
            "name": "chevron-down",
            "size": "16px",
            "color": "#7E8793"
          }
        },
        "menu": {
          "backgroundColor": "#FFFFFF",
          "borderRadius": "14px",
          "border": "1px solid rgba(215,234,245,0.9)",
          "shadow": "0px 14px 34px rgba(17,107,167,0.16)",
          "item": {
            "padding": "10px 12px",
            "textStyle": "body",
            "states": {
              "hover": { "backgroundColor": "#EAF2F8" },
              "active": { "backgroundColor": "#D7EAF5" },
              "selected": { "color": "#116BA7" }
            }
          }
        }
      }
    },
    "specificElements": {
      "waveIllustrations": {
        "usage": ["фон карточек", "фон экранов", "подложка в мини-тайлах"],
        "style": {
          "colors": ["rgba(21,152,213,0.25)", "rgba(104,220,242,0.35)", "rgba(234,242,248,0.9)"],
          "blur": "0px",
          "edgeSoftness": "high",
          "layering": "2-3 waves overlapped"
        }
      },
      "onboardingHero": {
        "composition": {
          "centerObject": "3D/realistic plastic water bottle",
          "background": "aquaHero gradient + abstract bubbles/waves",
          "cta": "круглая кнопка-стрелка внизу справа"
        },
        "ctaButton": {
          "type": "iconCircle",
          "size": "52px",
          "icon": "arrow-right",
          "iconSize": "22px",
          "backgroundColor": "rgba(37,38,49,0.85)",
          "iconColor": "#FFFFFF",
          "shadow": "0px 10px 24px rgba(37,38,49,0.20)",
          "states": {
            "pressed": { "transform": "scale(0.96)", "backgroundColor": "rgba(37,38,49,0.92)" },
            "disabled": { "opacity": "0.5" }
          }
        }
      },
      "drinkSelectorCard": {
        "largeMediaCard": {
          "size": {
            "height": "240px",
            "width": "100%"
          },
          "background": "waterWave gradient + photo/3D glass",
          "glassFillIndicator": {
            "text": "340/500 ml",
            "textStyle": {
              "fontFamily": "SF Pro Display",
              "fontSize": "16px",
              "fontWeight": "700",
              "color": "#252631"
            },
            "placement": "near top of glass",
            "contrastAssist": "soft highlight behind text (rgba(255,255,255,0.35))"
          },
          "plusButton": {
            "size": "44px",
            "backgroundColor": "rgba(255,255,255,0.78)",
            "border": "1px solid rgba(215,234,245,0.9)",
            "borderRadius": "9999px",
            "icon": "plus",
            "iconSize": "20px",
            "iconColor": "#252631",
            "shadow": "0px 8px 20px rgba(17,107,167,0.12)",
            "states": {
              "pressed": { "transform": "scale(0.96)" }
            }
          },
          "nextButton": {
            "type": "iconCircle",
            "size": "40px",
            "backgroundColor": "rgba(255,255,255,0.78)",
            "icon": "arrow-right",
            "iconSize": "18px",
            "iconColor": "#1598D5"
          }
        }
      },
      "statsTiles": {
        "tile": {
          "layout": "icon + value + label",
          "iconContainer": {
            "size": "36px",
            "backgroundColor": "rgba(234,242,248,0.95)",
            "borderRadius": "12px"
          },
          "valueStyle": "numericMedium",
          "labelStyle": "caption",
          "states": {
            "selected": {
              "border": "1px solid rgba(21,152,213,0.65)",
              "shadow": "0px 8px 20px rgba(17,107,167,0.12)"
            }
          }
        }
      },
      "accessibility": {
        "minTapTarget": "44px",
        "contrast": {
          "primaryOnWhite": "OK (blue on white)",
          "mutedText": "использовать #5A6170 для основного вторичного текста, #7E8793 только для подписей/лейблов"
        },
        "dynamicType": {
          "supported": true,
          "scaling": "iOS Text Styles mapping (headline/body/caption1)"
        }
      },
      "responsiveRules": {
        "breakpoints": [
          { "name": "small", "width": "320px" },
          { "name": "base", "width": "375px" },
          { "name": "large", "width": "390-428px" }
        ],
        "behavior": [
          "Карточки растягиваются по ширине контейнера с фиксированными внутренними паддингами.",
          "Сегмент-контрол занимает 100% ширины, элементы равновеликие.",
          "Кольцо прогресса центрируется, размер уменьшается на small до ~200px.",
          "Таббар фиксирован снизу, FAB перекрывает таббар по центру."
        ]
      }
    }
  }
}