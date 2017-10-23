
// Generated by CoffeeScript 1.6.2
(function() {
    (function($) {
        return $.widget('IKS.imageCaptionButton', {
            options: {
                uuid: '',
                editable: null
            },
            populateToolbar: function(toolbar) {
                var button, widget;

                widget = this;
                button = $('<span class="' + this.widgetName + '"></span>');
                button.hallobutton({
                    uuid: this.options.uuid,
                    editable: this.options.editable,
                    label: 'Image with Caption',
                    icon: 'icon-placeholder',
                    command: null
                });
                toolbar.append(button);
                return button.on('click', function(event) {
                    var insertionPoint, lastSelection, img_elem;

                    lastSelection = widget.options.editable.getSelection();
                    insertionPoint = $(lastSelection.endContainer).parentsUntil('.richtext').last();
                    var modal = ModalWorkflow({
                        url: window.chooserUrls.imageChooser + '?select_format=true',
                        responses: {
                            imageChosen: function(imageData) {

                                img_elem = $(imageData.html).get(0);


                            }
                        }
                    });

                    $('body > .modal').remove();
                    var container = $('<div class="modal fade editor" tabindex="-1" role="dialog" aria-hidden="true">\n    <div class="modal-dialog">\n        <div class="modal-content"\
>\n            <button type="button" class="close text-replace" data-dismiss="modal" aria-hidden="true"><i class="icon icon-cross"></i></button>\n            <div class="modal-body"><hea\
der class="nice-padding hasform"><div class="row"><div class="left"><div class="col"><h1><i class="icon icon-code"></i>&nbsp;Add A Caption</h1></div></header><div class="modal-bo\
dy-body"></div></div>\n        </div><!-- /.modal-content -->\n    </div><!-- /.modal-dialog -->\n</div>');

                    // add container to body and hide it, so content can be added to it before display
                    $('body').append(container);
                    container.modal('hide');
                    var modalBody = container.find('.modal-body-body');
                    modalBody.html('<p style=" margin: 2% 4%;">Leave blank for none</p><textarea placeholder="Caption" style="height: 200px; width: 92%; border: 1px solid #d8d8d8; background: #f4f4f4; margin: 2% 4%;" id="wagtail-edit-caption-content"></textarea><button i\
d="wagtail-edit-caption-save" type="button" style="margin: 0 4%; float: right;" class="button">Save</button>');
                    $("#wagtail-edit-caption-save").on("click", function() {

                        if ($('#wagtail-edit-caption-content').val() != '') {

                            var caption = document.createElement('p');
                            $(caption).addClass('caption');
                            $(caption).html($('#wagtail-edit-caption-content').val());
                            lastSelection.insertNode(caption);
                            widget.options.editable.setModified();


                        }

                        lastSelection.insertNode(img_elem);
                        if (img_elem.getAttribute('contenteditable') === 'false') {
                            insertRichTextDeleteControl(img_elem);
                        }
                        container.modal('hide');
                        return widget.options.editable.element.trigger('change');
                    });
                    container.modal('show');
                });
            }
        });
    })(jQuery);

}).call(this);