(function(){
    var factory = function (exports) {
        var lang = {
            name : "ru",
            description : "Онлайн Markdown редактор с открытым исходным кодом",
            tocTitle    : "Оглавление",
            toolbar : {
                undo             : "Отменить (Ctrl+Z)",
                redo             : "Повторить (Ctrl+Y)",
                bold             : "Жирный",
                del              : "Зачёркнутый",
                italic           : "Курсив",
                quote            : "Цитата",
                ucwords          : "Первую букву текста в верхниий регистр",
                uppercase        : "Выделенный текст в верхний регистр",
                lowercase        : "Выделенный текст в нижний регистр",
                h1               : "Заголовок #1",
                h2               : "Заголовок #2",
                h3               : "Заголовок #3",
                h4               : "Заголовок #4",
                h5               : "Заголовок #5",
                h6               : "Заголовок #6",
                "list-ul"        : "Неупорядоченный список",
                "list-ol"        : "Упорядоченный список",
                hr               : "Горизонтальная линия",
                link             : "Ссылка",
                "reference-link" : "Реферальная ссылка",
                image            : "Изображение",
                code             : "Код",
                "preformatted-text" : "Предварительно отформатированный текст / блок кода (отступ табуляции)",
                "code-block"     : "Блок кода (мультиязычный)",
                table            : "Таблицы",
                datetime         : "Дата и время",
                emoji            : "Эмодзи",
                "html-entities"  : "HTML-объекты",
                pagebreak        : "Разрыв страницы",
                watch            : "Скрыть панель предпросмотра",
                unwatch          : "Показать панель предпросмотра",
                preview          : "HTML предпросмотр (Shift + ESC для выхода)",
                fullscreen       : "Полноэкранный режим (ESC для выхода)",
                clear            : "Очистить",
                search           : "Поиск",
                help             : "Помощь",
                info             : "О редакторе" + exports.title
            },
            buttons : {
                enter  : "Ввод",
                cancel : "Отмена",
                close  : "Закрыть"
            },
            dialog : {
                link : {
                    title    : "Ссылка",
                    url      : "Адрес",
                    urlTitle : "Заголовок",
                    urlEmpty : "Ошибка: Пожалуйста, заполните адрес ссылки"
                },
                referenceLink : {
                    title    : "Реферальная ссылка",
                    name     : "Наименование",
                    url      : "Адрес",
                    urlId    : "Ид.",
                    urlTitle : "Заголовок",
                    nameEmpty: "Ошибка: Пожалуйста, заполните адрес ссылки",
                    idEmpty  : "Ошибка: Пожалуйста, заполните ид. ссылки",
                    urlEmpty : "Ошибка: Пожалуйста, заполните адрес ссылки"
                },
                image : {
                    title    : "Изображение",
                    url      : "Адрес",
                    link     : "Ссылка",
                    alt      : "Заголовок",
                    uploadButton     : "Загрузить",
                    imageURLEmpty    : "Ошибка: ссылка на изображение не может быть пустой",
                    uploadFileEmpty  : "Ошибка: изображение не может быть пустым",
                    formatNotAllowed : "Ошибка: разрешены изображения лишь с этим форматом:"
                },
                preformattedText : {
                    title             : "Преформатированный текст / Код",
                    emptyAlert        : "Ошибка: Пожалуйста, заполните преформатированный текст код",
                    placeholder       : "В процессе . . ."
                },
                codeBlock : {
                    title             : "Блок кода",
                    selectLabel       : "Языки: ",
                    selectDefaultText : "Выберите код языка",
                    otherLanguage     : "Другие языки",
                    unselectedLanguageAlert : "Ошибка: Пожалуйста, выберите код языка",
                    codeEmptyAlert    : "Ошибка: Пожалуйста, заполните блок кода",
                    placeholder       : "В процессе  . . ."
                },
                htmlEntities : {
                    title : "HTML-объекты"
                },
                help : {
                    title : "Помощь"
                }
            }
        };

        exports.defaults.lang = lang;
    };

	// CommonJS/Node.js
	if (typeof require === "function" && typeof exports === "object" && typeof module === "object")
    {
        module.exports = factory;
    }
	else if (typeof define === "function")  // AMD/CMD/Sea.js
    {
		if (define.amd) { // for Require.js

			define(["editormd"], function(editormd) {
                factory(editormd);
            });

		} else { // for Sea.js
			define(function(require) {
                var editormd = require("../editormd");
                factory(editormd);
            });
		}
	}
	else
	{
        factory(window.editormd);
	}

})();